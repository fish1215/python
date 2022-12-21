"""
============================
Author:yuquanyong(yqy)
Time:2022/12/8
E-mail:yuqy1205@163.com
============================
"""
import pytest
from api.api import test_json
from utils.log_util import logger
from utils.read import base_data


def test_post():
    logger.info("开始执行test_post方法")
    json_data = base_data.read_data()['json_data']
    result = test_json(json_data)
    # print("shuchu" + result)
    assert result['id'] == 101
    logger.info("用例执行完毕")

    # assert result['status'] == 0
    # assert result['msg'] == "ok"
    # assert result['result']["shouji"] == "13456755448"
    # assert result['result']["province"] == "浙江"
    # assert result['result']["city"] == "杭州"
    # assert result['result']["company"] == "中国移动"
    # assert result['result']["cardtype"] is None
    # assert result['result']["areacode"] == "0571"


# if __name__ == '__main__':
#     pytest.main()

