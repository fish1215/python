"""
============================
Author:yuquanyong(泉水)
Time:2022/11/28
E-mail:yuqy1205@163.com
============================
"""

import yaml

f = open("../config/data.yaml",encoding="utf-8")
data = yaml.safe_load(f)
# print(data)
# print(data["hero1"])
# print(data["hero2"])
# print(data["heros_name"])
# print(data["heros"])
# print(data["heros_name_list"])

print(data['test']["name"])
print(data['test']['request']['url'])
print(data['test']['request']['method'])
print(data['test']['request']['headers'])
print(data['test']['request']['json'])


print(data['mobile_belong'])

print(data['mobile_belong_post'])

print(data['mobile_belong_post'])

