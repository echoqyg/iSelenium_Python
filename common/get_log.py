#!/usr/bin/env python
# encoding: utf-8
import logging
import os


class GetLog:
    # 取上一个目录绝对路径
    _path_2 = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # 拼接路径
    _path_3 = os.path.join(_path_2, "log", "log.log")

    # 初始化生成器，设置格式
    def __init__(self):
        # 创建生成器
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.INFO)
        # 设置日志格式
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s",
                                           "%Y-%m-%d-%H:%M")

    def set_stream_handle(self):
        # 创建流处理器
        self.stream_handle = logging.StreamHandler()
        # 设置流处理器等级
        self.stream_handle.setLevel(logging.DEBUG)
        # 传入流处理器格式
        self.stream_handle.setFormatter(self.formatter)

    def set_file_handle(self):
        # 创建文件处理器的对象
        self.file_handle = logging.FileHandler(self._path_3)
        self.file_handle.setLevel(logging.DEBUG)
        # 设置文件处理器输出格式
        self.file_handle.setFormatter(self.formatter)

    def get_logger(self):
        # 调用方法
        self.set_stream_handle()
        self.set_file_handle()
        # 把流｜文件处理器，放入生成器
        self.logger.addHandler(self.stream_handle)
        self.logger.addHandler(self.file_handle)


log = GetLog()

if __name__ == '__main__':
    log = GetLog()
    log.get_logger()
    log.logger.debug("qian")
