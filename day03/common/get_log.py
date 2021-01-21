#!/usr/bin/env python
# encoding: utf-8
import logging


class GetLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s",
                                           "%Y-%m-%d-%H:%M")
        self.stream_handle = logging.StreamHandler()

    def set_stream_handle(self):
        self.stream_handle.setLevel(logging.DEBUG)
        self.stream_handle.setFormatter(self.formatter)
        self.logger.addHandler(self.stream_handle)


if __name__ == '__main__':
    log = GetLog()
    log.set_stream_handle()
    log.logger.debug("qian")
