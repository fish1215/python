"""
============================
Author:yuquanyong(yqy)
Time:2022/12/21
E-mail:yuqy1205@163.com
============================
"""
import allure
import pytest
from api.user_api import send_code
from utils.read import base_data

@allure.feature("用户中心模块")
class TestUser:
    @allure.title("注册手机号测试用例")
    @allure.story("用户注册后登录")
    def test_register(self):
        json_data = base_data.read_data()['test_register']
        result = send_code(json_data)
        print(json_data)
        assert result.success is True


