#!/usr/bin/env python
# encoding: utf-8
import logging


class GetLog:
    # 初始化生成器，设置格式
    def __init__(self):
        # 创建生成器
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.DEBUG)
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
        # 把流处理器，传入生成器
        self.logger.addHandler(self.stream_handle)


if __name__ == '__main__':
    log = GetLog()
    log.set_stream_handle()
    log.logger.debug("qian")
