#coding=utf-8
import os
import sys
import traceback

# 初始化
global GLOBAL_DICT
GLOBAL_DICT = {}

class Global:
    # 定义一个全局变量 
    @staticmethod
    def set_value(key,value):
        GLOBAL_DICT[key] = value
     
    # 获得一个全局变量,不存在则返回默认值
    @staticmethod
    def get_value(key, defValue=None):
        try:
            return GLOBAL_DICT[key]
        except KeyError:
            return defValue

