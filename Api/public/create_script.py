#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   create_script.py
 
@Time    :   2020/6/2 9:36 上午
'''
import os
import sys

from Api.getyaml.json_to_yaml import make_locustfile
from Api.settings import PROJECT_NAME,CASE_DIR

def create_script(project_name):
    project_name = project_name.upper()
    try:
        case_list = os.listdir(CASE_DIR)
    except FileNotFoundError:
        print('项目还没有创建！请使用 -start 命令创建项目，--help参考帮助')
        sys.exit(0)

    yaml_list = list(filter(lambda x : x[-5:].upper()=='.YAML',case_list))
    if project_name == PROJECT_NAME:

        if yaml_list:
            #处理文件后缀名
            cut_list = lambda x : x.upper().split('.YAML')[0]
            new_list = list()
            for _ in yaml_list:
                new_list.append(cut_list(_))

            r = map(make_locustfile,new_list)
            list(r)

        else:
            print('测试用例文件夹没有测试用例，请检查{case_dir}'.format(case_dir = CASE_DIR))

    else:
        print('当前输入项目名称与配置文件中的项目名称不符，请检查Api>settings.py文件中的PROJECT_NAME参数')

