#!/usr/bin/env python
# encoding: utf-8
import requests

id = "wwaabe2ad82255f238"
secret = "gRI4K5pjUX2R34YSKeK2CkMcvtluBO3OUQlWQaNPfNk"
url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={id}&corpsecret={secret}"

print(requests.get(url).json()["access_token"])

