#!/usr/bin/env python
# encoding: utf-8
import configparser
import os

from day01.get_token import get_token


class TestConfig():
    # 设置地址
    _path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    _path_2 = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    _path_3 = os.path.join(_path_2, "day01/config.ini")

    # 获取config.ini section, option的值
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self._path_3)
        return config.get('wechart', 'secret')

    # 修改config.ini section, option的值
    def set_config(self):
        config = configparser.ConfigParser()
        config.read(self._path_3)
        config.set('test', 'age', "2")
        config.write(open(self._path_3, "w"))


if __name__ == "__main__":
    # print(TestConfig().path_3)
    # print(os.getcwd())
    # print(os.path.join(os.getcwd(), "../.."))
    # print(get_token(TestConfig().get_config()))
    TestConfig().set_config()
