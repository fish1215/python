"""
============================
Author:yuquanyong(泉水)
Time:2022/11/28
E-mail:yuqy1205@163.com
Motto:努力学好每一节课程
============================
"""
import pytest

# 单次循环
# @pytest.mark.parametrize("key",values)
@pytest.mark.parametrize("key",["b"])
def test_paramtrize_01(key):
    # print("我是" + key)
    assert key == "a" or "b"

@pytest.mark.parametrize("her_name",["安其拉","黄忠","小乔"])
def test_paramtrize_01(her_name):

    assert her_name == "安其拉" or "黄忠" or "小乔"