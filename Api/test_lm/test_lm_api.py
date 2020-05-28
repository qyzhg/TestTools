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
        self._login_jituan()

    def _login_jituan(self):
        self.api('login_jituan')

    def test001(self):
        r = self.api('asyquery')
        print(r.json())

    def test002(self):
        r = self.api('login_sheshi504')
        print(r.text)