#!/usr/bin/env python
# encoding: utf-8
import allure
import pytest

from api.contact.member.member_api import MemberApi
from common.get_log import log

@allure.feature("用户管理测试")
class TestMember:
    member = MemberApi()

    @allure.story("新增用户测试")
    @pytest.mark.parametrize("userid,name,mobile,department,errcode,errmsg", [
        ("","zhangsan","13011134222",[1,2],41009,"missing userid"),
        ("zhangsan1","zhangsan","",[1,2],60129,"missing mobile")
    ], ids=["添加：缺少用户id","添加：缺少手机号"])
    def test_add_member(self,userid,name,mobile,department,errcode,errmsg):
        log.info("------------开始执行增加操作测试用例---------------")
        member_data = self.member.add_member_template(userid,name,mobile,department)
        assert errcode == member_data["errcode"]
        assert errmsg in member_data["errmsg"]

    @allure.story("删除用户测试")
    @pytest.mark.parametrize("userid,errcode,errmsg", [
        ("123",60111,"userid not found")
    ], ids=["删除：用户id未找到"])
    def test_delete_member(self,userid,errcode,errmsg):
        log.info("------------开始执行删除操作测试用例---------------")
        member_data = self.member.delete_member(userid)
        assert errcode == member_data["errcode"]
        assert errmsg in member_data["errmsg"]

    @allure.story("查询用户测试")
    @pytest.mark.parametrize("userid,errcode,errmsg", [
        ("123",60111,"userid not found")
    ], ids=["删除：用户id未找到"])
    def test_get_member(self,userid,errcode,errmsg):
        log.info("------------开始执行删除操作测试用例---------------")
        member_data = self.member.get_member(userid)
        assert errcode == member_data["errcode"]
        assert errmsg in member_data["errmsg"]

    @allure.story("新增用户非必填内容测试")
    @pytest.mark.parametrize("userid,name,mobile,department,position,gender,errcode,errmsg", [
        ("", "zhangsan", "13011134222", [1, 2], None,None,41009, "missing userid"),
        ("zhangsan1", "zhangsan", "", [1, 2], "None","None", 60129, "missing mobile")
    ], ids=["添加：缺少用户id", "添加：缺少手机号"])
    def test_add_member_(self, userid, name, mobile, department, position,gender, errcode, errmsg):
        log.info("------------开始执行增加操作测试用例---------------")
        member_data = self.member.add_member_template(userid, name, mobile, department,position,gender)
        assert errcode == member_data["errcode"]
        assert errmsg in member_data["errmsg"]