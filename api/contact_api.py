#!/usr/bin/env python
# encoding: utf-8
import requests

from api.base_api import BaseApi
from common.get_config import GetConfig


class ContactApi(BaseApi):
    def add_member(self):
        secret = GetConfig().get_config("wechart", "secret")
        # 增加成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token(secret)}"
        data_request = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1, 2]
        }
        res = requests.post(url=url, json=data_request)

    # 删除成员
    def delete_member(self):
        secret = GetConfig().get_value("wechart", "secret")
        token = self.get_token(secret)
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = f"access_token={token}&userid={self._id}"
        res = requests.get(url=url, params=params)
        return res.json()

    # 获取成员
    def get_member(self):
        pass

    # 编辑成员
    def edit_member(self):
        pass


if __name__ == '__main__':
    ContactApi().add_member()
