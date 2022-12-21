"""
============================
Author:yuquanyong(泉水)
Time:2022/11/28
E-mail:yuqy1205@163.com
============================
"""
import sys

import yaml
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

test_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "data.yaml")
print(test_path)


# base_path = os.path.dirname(os.path.abspath(__file__))
# print(base_path)
# sys.path.append(base_path)
# data_path = os.path.abspath(os.path.join(base_path, "../../../")) + "/config/datas/dataa.yaml"
# data_path1 = os.path.abspath(os.path.join(base_path, "config/datas/datas.yaml"))


def read_data():
    f = open(test_path, encoding="utf-8")
    data = yaml.safe_load(f)
    return data


get_data = read_data()
