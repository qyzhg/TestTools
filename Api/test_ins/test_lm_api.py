#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   test_lm_api.py
 
@Time    :   2020/5/27 4:27 下午
'''


import unittest
try:
    import requests
except ImportError:
    print('发现缺少的依赖库，正在尝试安装，如果安装失败，请使用pip install requests命令自行安装')
    import os
    os.system('pip install requests')
from Api.API import Api

class test_lm_api(unittest.TestCase,Api):
    def setUp(self) -> None:
        self.s = requests.Session()
        Api.__init__(self, self.s)


#Thu May 28 22:59:42 2020该代码由工具自动生成，请检查后使用！
    def test_testname(self):
        r = self.api('testname')

#Fri May 29 14:42:43 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:50:21 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:50:45 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:51:06 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:51:19 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:54:19 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 14:56:32 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 15:02:34 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 15:04:13 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 15:05:16 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

#Fri May 29 15:07:17 2020该代码由工具自动生成，请检查后使用！
    def test_test(self):
        r = self.api('test')

