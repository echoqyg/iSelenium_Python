#!/usr/bin/env python
# encoding: utf-8
import os
from pprint import pprint

import requests
import yaml

from api.base_api import BaseApi
from common.get_config import GetConfig, cf


class MemberApi(BaseApi):
    _member_path = "data/api/contact/member/dispose_member_template.yml"

    # def add_member(self):
    #     secret = GetConfig().get_config("wechart", "secret")
    #     # 增加成员
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token(secret)}"
    #     data_request = {
    #         "userid": "zhangsan",
    #         "name": "张三",
    #         "alias": "jackzhang",
    #         "mobile": "+86 13800000000",
    #         "department": [1, 2]
    #     }
    #     res = requests.post(url=url, json=data_request)

    # def add_member_by_yaml(self):
    #     secret = GetConfig().get_config("wechart", "secret")
    #     # yaml文件路径
    #     add_member_path = self.path_join(self.base_path, "data/api/contact/member/add_member.yml")
    #     # 读取路径
    #     with open(add_member_path, encoding="utf-8") as f:
    #         request = yaml.safe_load(f)
    #     # 更新url的值
    #     request["params"] = f"access_token={self.get_token(secret)}"
    #     # 增加成员
    #     print(request)
    #     res = self.request(request)
    #     return res

    def add_member_template(self, userid, name, mobile, department, position="", gender=""):
        secret = cf.get_config("wechart", "secret")
        data = {"token": self.get_token(secret), "userid": userid, "name": name,
                "mobile": mobile, "department": department, "position": position, "gender": gender}

        request_data = self.template_yml(self._member_path, data, "add")
        if request_data.get("json"):
            for k in request_data["json"].keys():
                if request_data["json"][k] == "None":
                    request_data["json"][k] = None
        return self.request(request_data)

    # 删除成员
    def delete_member(self, userid):
        secret = cf.get_config("wechart", "secret")
        token = self.get_token(secret)
        data = {"token": token, "userid": userid}
        request_data = self.template_yml(self._member_path, data, "delete")
        return self.request(request_data)

    # 获取成员
    def get_member(self, userid):
        secret = cf.get_config("wechart", "secret")
        token = self.get_token(secret)
        data = {"token": token, "userid": userid}
        request_data = self.template_yml(self._member_path, data, "get")
        return self.request(request_data)

    # 编辑成员
    def edit_member(self):
        pass


if __name__ == '__main__':
    # print(MemberApi().add_member_by_yaml())
    print(MemberApi().delete_member())

    """
    {'method': 'post', 'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create', 'params': 'access_token=_RyHAOzRGm3PdzYK-3A0CFUNX5xDiqU408iuhxOicrqn6suBavpKlLXacj-BTa51lySvv4bFXlJ2OT2YFwJA0yyervJSQdaCnEIn7llK-xmt_5wGFOk1L2tPAQaIsV7DsG4hTUkJuC1_xUtlzBscbCRxTbWO-rC3i6sVbaIi5O7tr39E3GMLcfvTVJ_5romRQoVnphFFWYGf5YsXsgsCVw', 'json': {'userid': 'zhangsan', 'name': '张三', 'alias': 'jackzhang', 'mobile': '+86 13800000000', 'department': [1, 2]}}
    {"errcode":60104,"errmsg":"mobile existed:zhangsan"}
    {'method': 'post', 'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create', 'params': 'access_token=_RyHAOzRGm3PdzYK-3A0CFUNX5xDiqU408iuhxOicrqn6suBavpKlLXacj-BTa51lySvv4bFXlJ2OT2YFwJA0yyervJSQdaCnEIn7llK-xmt_5wGFOk1L2tPAQaIsV7DsG4hTUkJuC1_xUtlzBscbCRxTbWO-rC3i6sVbaIi5O7tr39E3GMLcfvTVJ_5romRQoVnphFFWYGf5YsXsgsCVw', 'json': {'userid': 'zhangsan', 'name': '张三', 'alias': 'jackzhang', 'mobile': '+86 13800000000', 'department': '[1, 2]'}}
    {"errcode":40066,"errmsg":"Warning: wrong json format. invalid party list, hint: [1612356659_148_89bfe4261e97da2ba5ea42396c065e69], from ip: 221.196.89.223, more info at https://open.work.weixin.qq.com/devtool/query?e=40066"}

    """
