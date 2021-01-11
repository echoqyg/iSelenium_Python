#!/usr/bin/env python
# encoding: utf-8
import requests


def get_token(secret):
    id = "wwaabe2ad82255f238"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"

    return requests.get(url).json()["access_token"]
