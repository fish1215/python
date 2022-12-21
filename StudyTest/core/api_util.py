"""
============================
Author:yuquanyong(yqy)
Time:2022/12/8
E-mail:yuqy1205@163.com
============================
"""
from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get("/shouji/query", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

    # 以下是项目实战的方法
    def get_code(self,**kwargs):
        return  self.post("/code/",**kwargs)


api_util = Api()
