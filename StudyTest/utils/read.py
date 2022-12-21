"""
============================
Author:yuquanyong(yqy)
Time:2022/12/7
E-mail:yuqy1205@163.com
============================
"""
# import configparser
# import os
# import yaml
#
# data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data','data.yaml')
# ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","setting.ini")
#
# class FileRead:
#     def __int__(self):
#         self.data_path = data_path
#         self.ini_path = ini_path
#
#     def read_data(self):
#         f = open(self.data_path, encoding="utf8")
#         data = yaml.safe_load(f)
#         return data
#
#     def read_ini(self):
#         config = configparser.ConfigParser()
#         config.read(self.ini_path, encoding="utf8")
#         return config
#
# base_data = FileRead()
#
# print(data_path)
# print(ini_path)


import configparser
import os
import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "setting.ini")


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        # print(data)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config


base_data = FileRead()
# print(base_data.read_data())
# print(ini_path)
# print(base_data.read_ini()["host"]["api_sit_url"])