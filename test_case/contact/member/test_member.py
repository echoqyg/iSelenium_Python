#!/usr/bin/env python
# encoding: utf-8
from api.contact.member.member_api import MemberApi


class TestMember:
    def test_member(self):
        member = MemberApi().add_member_template()
        assert member["errcode"] == 60104
        assert member["errmsg"] == "mobile existed:zhangsan"
