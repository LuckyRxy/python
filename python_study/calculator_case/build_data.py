# todo: 构建输入数据
#
# @Time: 2024/12/30 15:57:10
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

import json

def build_data():
    test_data = []
    with open("./test_data.json", "r", encoding="UTF-8") as f:
        test_data = json.load(f)
    # print(test_data)
    return test_data


if __name__ == "__main__":
    build_data()