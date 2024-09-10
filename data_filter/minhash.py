import json
from datasketch import MinHash
import re
import os
import sys

# 定义一个函数来预处理文本
def preprocess_text(text):
    # 将文本转换为小写
    text = text.lower()
    # 删除非字母数字字符
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # 分割成单词
    words = text.split()
    return words

# 定义一个函数来计算两个 origin_prompt 列表的平均 MinHash 相似度
def average_minhash_similarity(origin_prompt_1, origin_prompt_2):
    m1 = MinHash(num_perm=128)
    m2 = MinHash(num_perm=128)

    # 更新 MinHash 结构
    for content_1 in origin_prompt_1:
        words = preprocess_text(content_1['content'])
        for word in words:
            m1.update(word.encode('utf8'))

    for content_2 in origin_prompt_2:
        words = preprocess_text(content_2['content'])
        for word in words:
            m2.update(word.encode('utf8'))

    # 计算相似度
    return m1.jaccard(m2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        data = json.load(file)
        # 设置 MinHash 相似度阈值
        threshold = 0.7

        # 存储已经处理过的 key
        processed_keys = []

        # 存储需要删除的键
        keys_to_delete = []

        # 遍历 JSON 数据并检查相似性
        for key1, value1 in data.items():
            if key1 not in processed_keys:
                for key2, value2 in data.items():
                    if key2 != key1 and key2 not in processed_keys:
                        sim = average_minhash_similarity(value1['origin_prompt'], value2['origin_prompt'])
                        if sim >= threshold:
                            print(f"Removing {key2} because it is similar to {key1} with similarity {sim:.2f}")
                            keys_to_delete.append(key2)
                            processed_keys.append(key2)

        # 删除相似的键
        for key in keys_to_delete:
            del data[key]

        # 写入新的 JSON 文件
        data_json = json.dumps(data, ensure_ascii=False)
        name, ext = os.path.splitext(file_name)
        with open(f'{name}_minhash.json', 'w', encoding="utf8") as file_new:
            file_new.write(data_json)

if __name__ == "__main__":
    main()
