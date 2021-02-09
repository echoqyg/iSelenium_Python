#!/usr/bin/env python
# encoding: utf-8
import configparser
import os


class GetConfig():
    # 设置地址 取上上个目录的绝对路径
    _path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #取上一个目录绝对路径
    _path_2 = os.path.abspath(os.path.join(os.getcwd(), ".."))
    #拼接路径
    _path_3 = os.path.join(_path, "config.ini")

    # 获取config.ini section, option的值
    def get_config(self,section, option):
        config = configparser.ConfigParser()
        config.read(self._path_3)
        return config.get(section, option)

    # 修改config.ini section, option的值
    def set_config(self):
        config = configparser.ConfigParser()
        config.read(self._path_3)
        config.set('test', 'age', "2")
        config.write(open(self._path_3, "w"))


if __name__ == "__main__":
    print(GetConfig()._path)
    # print(os.getcwd())
    # print(os.path.join(os.getcwd(), "../.."))
    # print(get_token(TestConfig().get_config()))
    # TestConfig().set_config()
