#!/usr/bin/env python
# encoding: utf-8
import configparser
import os

from day01.get_token import get_token


class TestConfig():
    _path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    _path_2 = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    _path_3 = os.path.join(_path_2, "day01/config.ini")

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(self._path_3)
        return config.get('wechart', 'secret')


if __name__ == "__main__":
    # print(TestConfig().path_3)
    # print(os.getcwd())
    # print(os.path.join(os.getcwd(), "../.."))
    print(get_token(TestConfig().get_config()))