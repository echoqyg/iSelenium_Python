#!/usr/bin/env python
# encoding: utf-8
import logging
import os
import time

from common.get_config import cf


class GetLog:
    # 取上一个目录绝对路径
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    log_level = cf.get_config_int("log", "level")
    file_mode = cf.get_config("log", "mode")

    # 初始化生成器，设置格式
    def __init__(self):
        # 创建生成器
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(self.log_level)
        # 设置日志格式
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s",
                                           "%Y-%m-%d-%H:%M")

    def set_stream_handle(self):
        # 创建流处理器
        self.stream_handle = logging.StreamHandler()
        # 设置流处理器等级
        self.stream_handle.setLevel(self.log_level)
        # 传入流处理器格式
        self.stream_handle.setFormatter(self.formatter)

    def set_file_handle(self):
        # 时间戳按照时间格式数据，作为文件名
        file_name = time.strftime("%Y-%m-%d_%H", time.localtime(time.time()))
        # 拼接路径
        path = os.path.join(self.base_path, "log", f"{file_name}.log")
        # 创建文件处理器的对象
        self.file_handle = logging.FileHandler(path, mode=self.file_mode)
        self.file_handle.setLevel(self.log_level)
        # 设置文件处理器输出格式
        self.file_handle.setFormatter(self.formatter)

    def get_logger(self):
        # 调用方法
        self.set_stream_handle()
        self.set_file_handle()
        # 把流｜文件处理器，放入生成器
        self.logger.addHandler(self.stream_handle)
        self.logger.addHandler(self.file_handle)
        return self.logger


log = GetLog().get_logger()

if __name__ == '__main__':
    log.debug("qian")
