#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   make_project.py
 
@Time    :   2020/6/1 10:40 上午
'''
import os
from shutil import copyfile
from Api.settings import TEMPLATE_DIR

def make_locust_project(locust_dir):
    if os.path.isdir(locust_dir):
        print('新建locust项目失败！\n{locust_dir}目录已存在，请检查路径！'.format(locust_dir = locust_dir))
    else:
        #新建locust项目目录
        os.makedirs(locust_dir)
        print('新建locust目录成功!\n{locust_dir}\n使用时请在Api>settings中将项目自行注册到LOCUSTFILE_DIR中'.format(locust_dir = locust_dir))
        make_locust_files(locust_dir)


def make_test_api_dir(test_api_dir):
    if os.path.isdir(test_api_dir):
        print('新建test_api项目失败！\n{test_api_dir}目录已存在，请检查路径！'.format(test_api_dir=test_api_dir))
    else:
        # 新建test_api项目目录
        os.makedirs(test_api_dir)
        print('新建test_api目录成功!\n{test_api_dir}\n使用时请在Api>settings中将项目自行注册到TEST_API_DIR中'.format(test_api_dir=test_api_dir))
        make_test_api_files(test_api_dir)


def make_locust_files(locust_dir):
    old_init_file = os.path.join(TEMPLATE_DIR,'__init__.py')
    new_init_file = os.path.join(locust_dir,'__init__.py')
    copyfile(old_init_file,new_init_file)
    print('在{locust_dir}中生成初始化文件成功！'.format(locust_dir = locust_dir))
    old_locust_file = os.path.join(TEMPLATE_DIR,'locustfile.py')
    new_locust_file = os.path.join(locust_dir,'locustfile.py')
    copyfile(old_locust_file,new_locust_file)
    print('在{locust_dir}中生成locustfile文件成功！'.format(locust_dir=locust_dir))


def make_test_api_files(test_api_dir):
    old_init_file = os.path.join(TEMPLATE_DIR,'__init__.py')
    new_init_file = os.path.join(test_api_dir,'__init__.py')
    copyfile(old_init_file,new_init_file)
    print('在{test_api_dir}中生成初始化文件成功！'.format(test_api_dir = test_api_dir))
    old_test_api = os.path.join(TEMPLATE_DIR,'test_api.py')
    new_test_api = os.path.join(test_api_dir,'test_api.py')
    copyfile(old_test_api,new_test_api)
    print('在{test_api_dir}中生成test_api文件成功！'.format(test_api_dir=test_api_dir))