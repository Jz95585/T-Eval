import json
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        data = json.load(file)
        data1={}
        for key,value in data.items():
            new_key = key + "_1"
            data1[new_key] = value

        # 写入新的 JSON 文件
        data_json = json.dumps(data1, ensure_ascii=False)
        name, ext = os.path.splitext(file_name)
        with open(f'{name}_changed.json', 'w', encoding="utf8") as file_new:
            file_new.write(data_json)

if __name__ == "__main__":
    main()
