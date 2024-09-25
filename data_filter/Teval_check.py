import json
import sys
import os
import time
#import configparser
from typing import List

#import openai
from openai import OpenAI
#import openai.error as openai_error
import pandas as pd
from tqdm import tqdm
 
#import my_secrets


#openai.api_key = my_secrets.OPENAI_API_KEY
TEXT_DAVINCI_003 = "text-davinci-003"
CHAT_GPT_35_TURBO = "gpt-3.5-turbo"
GPT4 = "gpt-4"

class Config:
    """
    Class to read the config file and store the parameters.
    """
    def __init__(self):
        #self.config: configparser.ConfigParser = self.read_config(config_file)
        self.input_path: str = "/mnt/data3/finLLM/agent_framework/T-Eval/data1/agent_final数据/reason_checked_zh.json"
        self.output_path: str = "/mnt/data3/finLLM/agent_framework/T-Eval/data1/agent_final数据/reason_checked_zh.json"
        self.num_examples: int = 1000
        self.jaccard_threshold: float = 0.8
        # self.model: str = "gpt-3.5-turbo"
        # self.model: str = "Glm-4-Flash"
        self.model: str = "deepseek-chat"
        self.temperature: float = 0.01
        self.top_p: float = 1
        self.frequency_penalty: float = 0
        self.presence_penalty: float = 0
        self.stop: List[str] = []
        self.max_tokens: int = 1024
        self.starting_sample: int = 0

    # @staticmethod
    # def read_config(config_file: str) -> configparser.ConfigParser:
    #     config: configparser.ConfigParser = configparser.ConfigParser()
    #     config.read(config_file)
    #     return config

def ask_for_confirmation(prompt: str) -> bool:
    """
    Ask the user for confirmation.
    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        bool: True if the user entered 'y' or 'yes', False if the user entered 'n' or 'no'.
    """
    while True:
        user_input = input(f"{prompt} (y/n): ").lower()
        if user_input in ["yes", "y"]:
            return True
        elif user_input in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def read_alpaca_data_json(filename: str, num_samples: int, starting_sample: int = 0) -> dict:
    """
    Read Alpaca data from a JSON file.

    Args:
        filename: The path to the JSON file.
        num_samples: The number of samples to read.
        starting_sample: The index of the first sample to read.

    Returns:
        A pandas DataFrame containing the data.
    """

    print(f"Reading {filename}...")
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print("Read data successfully.")
    return data

def openai_gpt(prompt: str, config, verbose: bool = False, max_attempts: int = 3) -> str:
    """
    This function sends a prompt to the OpenAI GPT API and returns the response.
    It tries the creation several times (max_attempts) in case of exception.
    If the model is text-davinci-003, it uses the Completion API, otherwise it uses the ChatCompletion API.

    Args:
        prompt (str): Prompt to send to the API.
        config (_type_): Configuration object.
        verbose (bool, optional): If True, print the prompt and response. Defaults to False.
        max_attempts (int, optional): Number of attempts to make in case of exception. Defaults to 3.

    Returns:
        str: The response from the API.
    """
    # send the prompt to gpt and return the response
    # try the creation several times in case of exception
    for attempt in range(1, max_attempts + 1):
        # try:
            # if config.model == TEXT_DAVINCI_003:
            #     response = openai.Completion.create(
            #         model=config.model,
            #         prompt=prompt,
            #         max_tokens=config.max_tokens,
            #         temperature=config.temperature,
            #         top_p=config.top_p,
            #         frequency_penalty=config.frequency_penalty,
            #         presence_penalty=config.presence_penalty,
            #         stop=config.stop
            #     )
            #     choices = [choice["text"] for choice in response["choices"]]
            # elif config.model == CHAT_GPT_35_TURBO or config.model == GPT4:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
        ]
        # response = openai.ChatCompletion.create(
        #     model=config.model,
        #     messages=messages,
        #     max_tokens=config.max_tokens,
        #     temperature=config.temperature,
        #     top_p=config.top_p,
        #     frequency_penalty=config.frequency_penalty,
        #     presence_penalty=config.presence_penalty,
        #     stop=config.stop
        # )
        client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url = os.environ["OPENAI_API_BASE"]
        )
        response = client.chat.completions.create(
            model=config.model,
            messages=messages,
            max_tokens=config.max_tokens,
            temperature=config.temperature,
            top_p=config.top_p,
            frequency_penalty=config.frequency_penalty,
            presence_penalty=config.presence_penalty,
            stop=config.stop
        )
        # choices = [choice["message"]["content"] for choice in response["choices"]]

        if verbose:
            print("*" * 20)
            print(f"Model: {config.model}")
            print(f"Prompt: {prompt}")
            print(f"Response: {response['choices'][0]['text']}")

        # return choices[0]
        return response.choices[0].message.content
        # except openai_error.OpenAIError as e:
        #     if attempt < max_attempts:
        #         print(f"Error on attempt {attempt}: {e}. Retrying...")
        #         time.sleep(2)  # Wait for 2 seconds before retrying
        #     else:
        #         print(f"Error on attempt {attempt}: {e}. All attempts failed.")
        #         # we will return None if all attempts failed because raising an exception will stop the program and we will lose all the data we have collected so far
        #         return None

def generate_prompt(row) -> str:
    """ Generate the prompt for the row.

    Args:
        row (_type_): The row of the dataframe.

    Returns:
        str: The prompt generated from the row.
    """
    # generate the prompt for the row
    instruction = row["origin_prompt"][0]["content"]
    input_data = row["origin_prompt"][1:]
    # #understand数据
    # output_data = row["ground_truth"]['args']
    # #review数据
    # output_data = row["ground_truth"]['answer']
    # #retrieve数据
    # output_data = row["ground_truth"]['name']
    #reason数据
    output_data = row["ground_truth"]['thought']
    # #instruct,plan不筛选,rru数据
    # output_data = row["ground_truth"]

    if input_data != "" or input_data == "Noinput":
        prompt = f"Following the format <yes/no>||<explanation why yes or no>. Given the following instruction: {instruction} and the following input: {input_data}, is the output '{output_data}' correct?"
    else:
        prompt = f"Following the format <yes/no>||<explanation why yes or no>. Given the following instruction: {instruction}, is the output '{output_data}' correct?"
    return prompt

def read_output_file(output_file: str) -> pd.DataFrame:
    data = pd.read_csv(output_file)
    print(f"Data not checked against GPT. Using the results from {output_file}.")
    return data

def save_data_to_csv(data: pd.DataFrame, output_file: str) -> None:
    print(f"Saving data to {output_file}...")
    data.to_csv(output_file, index=False)

def save_data_to_json(data: dict, output_file: str) -> None:
    print(f"Saving data to {output_file}...")
    data_json = json.dumps(data, ensure_ascii=False)
    with open(output_file, 'w', encoding="utf8") as file_new:
            file_new.write(data_json)

def main():
    try:
        # read the config file
        config: Config = Config()

        data = read_alpaca_data_json(config.input_path, config.num_examples)
        count = 0
        processed_keys = []
        for key, value in data.items():
            response_gpt = openai_gpt(prompt=generate_prompt(value), config=config, verbose=False)
            print("response_gpt:")
            print(response_gpt)
            if "no||" in response_gpt or "No||" in response_gpt or "<no>||" in response_gpt or "<No>||" in response_gpt:
               processed_keys.append(key)
        for key in processed_keys:
           del data[key]
           count+=1
        print("总共筛选掉了")
        print(count)
        print("条数据")
        save_data_to_json(data, config.output_path)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
