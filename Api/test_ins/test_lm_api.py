#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   test_lm_api.py
 
@Time    :   2020/5/27 4:27 下午
'''


import unittest
import requests
from Api.API import Api

class test_lm_api(unittest.TestCase,Api):
    def setUp(self) -> None:
        self.s = requests.Session()
        Api.__init__(self, self.s)

#该代码由工具自动生成，请检查后使用！
    def testtest(self):
        r = self.api('test')

