#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   test_lm_api.py
 
@Time    :   2020/5/27 4:27 下午
'''

import sys
import unittest
import os
try:
    import requests
except ImportError:
    print('发现缺少的依赖库，正在尝试安装，如果安装失败，请使用pip install requests命令自行安装')
    os.system('pip install requests')
sys.path.append(os.path.abspath('../..'))
from Api.API import Api

class test_lm_api(unittest.TestCase,Api):
    def setUp(self) -> None:
        self.s = requests.Session()
        Api.__init__(self, self.s)
        self.test_login_sheshi()


#Fri May 29 16:20:00 2020该代码由工具自动生成，请检查后使用！
    def test_login_sheshi(self):
        r = self.api('login_sheshi')
        print(r.text)

#Fri May 29 16:25:17 2020该代码由工具自动生成，请检查后使用！
    def test_licenseBusiness_asyListQuery(self):
        r = self.api('licenseBusiness_asyListQuery')

