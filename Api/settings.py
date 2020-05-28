#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   settings.py
 
@Time    :   2020/5/28 8:50 上午
'''


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HOST = 'http://10.102.111.117:8093/HCLCNNC/a/'

CASE_DIR = os.path.join(BASE_DIR,'test_case')

LOCUSTFILE_DIR = os.path.join(BASE_DIR, 'locust_item_ins')

TEST_API_DIR = os.path.join(BASE_DIR,'test_ins')