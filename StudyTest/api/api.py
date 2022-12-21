"""
============================
Author:yuquanyong(yqy)
Time:2022/12/8
E-mail:yuqy1205@163.com
============================
"""
import json

from core.api_util import api_util
from utils.log_util import logger
from utils.response_util import process_response


# A方法
def mobile_query(params):
    response = api_util.get_mobile_belong(params=params)
    result = process_response(response)
    return result

def test_json(json_data):
    """
    这个方法测试post传参
    :param json_data:
    :return:
    """
    response = api_util.post_data(json=json_data)
    result = process_response(response)
    return  result



