#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   测试写入.py
 
@Time    :   2020/5/28 1:59 下午
'''


import unittest
import requests
from Api.API import Api

class test_lm_api(unittest.TestCase,Api):
    def setUp(self) -> None:
        self.s = requests.Session()
        self._login_jituan()

    def _login_jituan(self):
        self.api('login_jituan')

    def test001(self):
        r = self.api('asyquery')
        print(r.json())

    def test002(self):
        r = self.api('login_sheshi504')



#该代码由工具自动生成，请检查后使用！
    def testinspectionItem_asyQuery(self):
        r = self.api('inspectionItem_asyQuery')

#该代码由工具自动生成，请检查后使用！
    def testinspectionItem_asyQuery(self):
        r = self.api('inspectionItem_asyQuery')

#该代码由工具自动生成，请检查后使用！
    def testinspectionItem_asyQuery(self):
        r = self.api('inspectionItem_asyQuery')

