#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   test_api_dir.py
 
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
    import requests
sys.path.append(os.path.abspath('../..'))
from Api.public.API import Api

class test_api(unittest.TestCase, Api):
    def setUp(self) -> None:
        self.s = requests.Session()

#Mon Jun  1 10:00:44 2020该代码由工具自动生成，请检查后使用！
    def test_login_POST_DATA(self):
        r = self.api('login_POST_DATA.yaml')
        print(r.text)