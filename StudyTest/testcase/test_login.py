"""
============================
Author:yuquanyong(泉水)
Time:2022/11/27
E-mail:yuqy1205@163.com
Motto:努力学好每一节课程
============================
"""
import pytest


def test_login():
    print("login...")

@pytest.mark.run(order=2)
def test_search():
    print("search...")

@pytest.mark.run(order=1)
def test_order():
    print("order...")

@pytest.mark.run(order=3)
def test_pay():
    print("pay...")