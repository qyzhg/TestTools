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

LOCUSTFILE_DIR = os.path.join(BASE_DIR, 'locust_item')

LOCUSTFILE_FILE = os.path.join(LOCUSTFILE_DIR,'locustfile.py')

TEST_API_DIR = os.path.join(BASE_DIR,'test_api')

TEST_API_FILE = os.path.join(TEST_API_DIR,'test_api.py')

JSON_FILE = os.path.join(BASE_DIR,'getyaml','json')

