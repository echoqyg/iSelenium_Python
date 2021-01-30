#!/usr/bin/env python
# encoding: utf-8
import os

import requests


class BaseApi:
    _id = "wwaabe2ad82255f238"
    # 定义一个绝对路径，让其他子类都可以使用
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #静态方法，不使用类的属性和方法，不使用对象的属性和方法
    @staticmethod
    def static_method():
        pass

    def get_token(self,secret):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._id}&corpsecret={secret}"

        return requests.get(url).json()["access_token"]

    def request(self,request):
        res = requests.request(**request)
        return res

    def path_join(self,path,join_path):
        return os.path.join(path,join_path)

if __name__ == '__main__':
    print(BaseApi().base_path)