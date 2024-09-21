import json
import os
import sys
import random
#使各个任务的数据数量保持一致
def filter_keys(data, num_keys_to_keep=200):
    """
    递归地遍历字典，并随机选择num_keys_to_keep个键进行保留。
    
    :param data: 要过滤的字典或列表。
    :param num_keys_to_keep: 需要保留的键的数量。
    :return: 过滤后的字典或列表。
    """
    if isinstance(data, dict):
        # 获取所有键的列表
        keys = list(data.keys())
        
        # 如果键的数量小于或等于需要保留的数量，则直接返回原字典
        if len(keys) <= num_keys_to_keep:
            return {k: filter_keys(v, num_keys_to_keep) for k, v in data.items()}
        
        # 随机选择需要保留的键
        keys_to_keep = random.sample(keys, num_keys_to_keep)
        
        # 创建一个新的字典，只包含选中的键
        filtered_data = {k: filter_keys(data[k], num_keys_to_keep) for k in keys_to_keep}
        return filtered_data
    
    elif isinstance(data, list):
        # 对于列表中的每个元素递归调用filter_keys
        return [filter_keys(item, num_keys_to_keep) for item in data]
    
    else:
        # 如果是其他类型（如字符串、数字等），直接返回
        return data


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    # 读取JSON数据
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # 随机选择并保留200个键
        filtered_data = filter_keys(data, num_keys_to_keep=200)

        # 写入新的 JSON 文件
        data_json=json.dumps(filtered_data, ensure_ascii=False)
        name, ext = os.path.splitext(file_name)
        with open(f'{name}_final_zh.json', 'w', encoding="utf8") as file_new:
             file_new.write(data_json)


if __name__ == "__main__":
    main()
