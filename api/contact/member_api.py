#!/usr/bin/env python
# encoding: utf-8
import os
from pprint import pprint

import requests
import yaml

from api.base_api import BaseApi
from common.get_config import GetConfig


class MemberApi(BaseApi):
    # def add_member(self):
    #     secret = GetConfig().get_config("wechart", "secret")
    #     # 增加成员
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token(secret)}"
    #     data_request = {
    #         "userid": "zhangsan",
    #         "name": "张三",
    #         "alias": "jackzhang",
    #         "mobile": "+86 13800000000",
    #         "department": [1, 2]
    #     }
    #     res = requests.post(url=url, json=data_request)

    def add_member_by_yaml(self):
        secret = GetConfig().get_config("wechart", "secret")
        #yaml文件路径
        add_member_path = self.path_join(self.base_path, "data/api/contact/member/add_member.yml")
        #读取路径
        with open(add_member_path, encoding="utf-8") as f:
            request = yaml.safe_load(f)
        #更新url的值
        request["url"]=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token(secret)}"
        # 增加成员
        res = self.request(request)
        return res.text
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
    print(MemberApi().add_member_by_yaml())
