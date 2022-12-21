"""
============================
Author:yuquanyong(泉水)
Time:2022/11/27
E-mail:yuqy1205@163.com
Motto:努力学好每一节课程
============================
"""

import  pytest

@pytest.mark.P0
def test_one():
    expect = 1
    acture = 2
    assert expect == acture

@pytest.mark.test
def test_two():
    expect =1
    acture =1
    assert expect == acture