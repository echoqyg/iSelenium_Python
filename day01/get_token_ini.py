#!/usr/bin/env python
# encoding: utf-8
import configparser

from day01.get_token import get_token

config = configparser.ConfigParser()
path = "config.ini"
config.read(path)
secret = config.get('wechart', 'secret')
print(get_token(secret))
