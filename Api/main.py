#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao

@Contact :   qyzhg@163.com

@File    :   main.py

@Time    :   2020/5/30 5:27 下午
'''


import argparse
import os
import sys
sys.path.append(os.path.abspath('../'))
from Api.public.menu import menu
from Api.settings import *
from Api.public.make_project import make_locust_project,make_test_api_dir


parser = argparse.ArgumentParser(description='先将需要转换的json放入json文件中 命令为python --n 接口名 --u 接口地址 --m 请求方式')
parser.add_argument('--n', type=str,help='接口名，例如：login，输入@auto可以根据接口地址自动生成接口名')
parser.add_argument('--u', type=str,help='接口地址，例如：a/login，配置好settings中的HOST后，可以直接输入完整地址')
parser.add_argument('--m', type=str,help='请求方式，只能输入三种请求方式：GET，POST/data，POST/json')
parser.add_argument('-start',type=str,help='生成项目目录')

args = parser.parse_args()

start = args.start
if start:
    locust_dir,test_api_dir = (os.path.join(BASE_DIR,'locust_dir_'+start)),(os.path.join(BASE_DIR,'test_api_'+start))
    make_locust_project(locust_dir)
    make_test_api_dir(test_api_dir)
    sys.exit(0)




#获取参数
#处理带有前缀的URL
url = args.u
if url == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)
if HOST in url:
    url = url.split(HOST)[1]
meth = args.m
if meth == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)
name = args.n
if name == None:
    print('请带参数运行此工具，需要帮助请使用--help命令')
    sys.exit(0)
if name == '@auto':
    name = (url + '_' + meth.upper()).replace('/','_')
#yaml输出路径
case_path = os.path.join(CASE_DIR,name) + '.yaml'


if None in [name,url,meth]:
    print('缺少必要的参数，请使用--help参数查看帮助')
    sys.exit(0)

#测试用例已存在
if os.path.isfile(case_path):
    print('目录中已存在同名测试用例文件：{case_path},请选择是否覆盖??'.format(case_path = case_path))
    while True:
        is_replace = input('Y:覆盖(默认) \nN:取消操作\n').upper()
        if is_replace == 'Y' or is_replace == 'YES' or is_replace == '':
            menu(name=name,url=url,meth=meth,case_path=case_path)
            break
        elif is_replace == 'N' or is_replace == 'NO':
            print('已取消操作！')
            sys.exit(0)
        else:
            print('输入有误，请重新选择')
#测试用例不存在
else:
    menu(name=name, url=url, meth=meth, case_path=case_path)