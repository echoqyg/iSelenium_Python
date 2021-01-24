#!/usr/bin/env python
# encoding: utf-8
import requests


class BaseApi:
    _id = "wwaabe2ad82255f238"
    #静态方法，不使用类的属性和方法，不使用对象的属性和方法
    @staticmethod
    def static_method():
        pass

    def get_token(self,secret):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self._id}&corpsecret={secret}"

        return requests.get(url).json()["access_token"]
