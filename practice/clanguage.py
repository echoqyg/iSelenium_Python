#!/usr/bin/env python
# encoding: utf-8
class Clanguage():
    # 定义对象属性
    class_name = "钱钱"

    # 定义市里方法
    def info(self, name):
        print(name, "向你问好")

    # 构造函数
    def __init__(self):
        print("默默想念你")

    # 类方法
    @classmethod
    def class_info(cls):
        print("正在调用类方法", cls)

    # 静态方法没有类似 self、cls 这样的特殊参数，
    # 因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。
    # 也正因为如此，类的静态方法中无法调用任何类属性和类方法。
    @staticmethod
    def static_info():
        print("正在调用静态方法")


if __name__ == '__main__':
    a = Clanguage()
    a.info("钱钱")
    a.class_info()
    a.static_info()
