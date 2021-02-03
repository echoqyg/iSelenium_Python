#!/usr/bin/env python
# encoding: utf-8
import os
from string import Template

import requests

from common.get_config import GetConfig
from common.get_log import GetLog


class BaseApi:
    _id = "wwaabe2ad82255f238"
    # 定义一个绝对路径，让其他子类都可以使用
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    from common.get_log import log
    logger = log.get_logger()

    # 静态方法，不使用类的属性和方法，不使用对象的属性和方法
    @staticmethod
    def static_method():
        pass

    def get_token(self, secret):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._id}&corpsecret={secret}"

        return requests.get(url).json()["access_token"]

    def request(self, request):
        res = requests.request(**request)
        return res

    def path_join(self, path, join_path):
        return os.path.join(path, join_path)

    # 使用Template方法替换yml重的变量
    def template_yml(self, r_data: dict, data: dict):
        return Template(str(r_data)).substitute(data)


if __name__ == '__main__':
    print(BaseApi().base_path)
