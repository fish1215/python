"""
============================
Author:yuquanyong(泉水)
Time:2022/11/28
E-mail:yuqy1205@163.com
Motto:努力学好每一节课程
============================
"""
import pytest


# #  数组的形式
# @pytest.mark.parametrize("name,word", [["安其拉","火烧屁屁啦"],["黄忠","周日让我射熄火了"],["鲁班","上下左右"]])
# def test_parametrize_03(name,word):
#     # print(f'{name}的台词是{word}')
#     print('{}的台词{}'.format(name,word))
#
#
# # 元组的形式
# @pytest.mark.parametrize("name,word", [("安其拉","火烧屁屁啦"),("黄忠","周日让我射熄火了"),("鲁班","上下左右")])
# def test_parametrize_03(name,word):
#     # print(f'{name}的台词是{word}')
#     print('{}的台词{}'.format(name,word))


# @pytest.mark.parametrize("name,word", [["安其拉","火烧屁屁啦"]])
# def test_parametrize_03(name,word):
#     # print(f'{name}的台词是{word}')
#     print('{}的台词{}'.format(name,word))


# 参数为字典
@pytest.mark.parametrize("hero", [{"name":"安其拉"},{"name":"黄忠"},{"name":"鲁班"}])
def test_parametrize_03(hero):
    # print(f'{name}的台词是{word}')
    print(hero["name"])