"""
============================
Author:yuquanyong(yqy)
Time:2022/12/7
E-mail:yuqy1205@163.com
============================
"""

import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config","setting.ini")

def read_ini ():
    config = configparser.ConfigParser()
    config.read(path,encoding='utf8')
    return config

get_ini = read_ini()

print(read_ini()['host']['api_sit_url'])
