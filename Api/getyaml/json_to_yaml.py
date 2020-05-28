#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   测试yaml.py
 
@Time    :   2020/5/26 10:39 上午
'''

import ruamel.yaml
import ast
import argparse
import os
import sys
sys.path.append(os.path.abspath('../..'))
from Api.settings import *
from Api.WriteTestCase import WriteTestCase

parser = argparse.ArgumentParser(description='先将需要转换的json放入json文件中 命令为python --n 接口名 --u 接口地址 --m 请求方式')
parser.add_argument('--n', type=str,help='接口名，例如：login')
parser.add_argument('--u', type=str,help='接口地址，例如：a/login')
parser.add_argument('--m', type=str,help='请求方式，只能输入三种请求方式：GET，POST/data，POST/json')

args = parser.parse_args()
#获取参数
name = args.n
url = args.u
meth = args.m
#yaml输出路径
case_path = os.path.join(CASE_DIR,name) + '.yaml'
#性能文件路径
locustfile_path = os.path.join(LOCUSRFILE_DIR,'测试写入.py')
#接口测试文件路径
test_api_path = os.path.join(TEST_API_DIR,'测试写入.py')



def json_to_yaml(name,url,meth):
    with open('json', 'r', encoding='utf-8') as f:
        dict_f = ast.literal_eval(str(f.read()))
        dict_var = {
                    'name':name,
                    'url':url,
                    'meth':meth,
                    'params':
                        dict_f
                    }
    with open(case_path,'w+',encoding='utf-8') as case_file:
        print(ruamel.yaml.dump(dict_var,Dumper=ruamel.yaml.RoundTripDumper,allow_unicode=True),file=case_file)
        print('已生成接口配置文件：'+case_path)
        WriteTestCase(filepath=locustfile_path,
                      linenum=-4,
                      content="\n#该代码由工具自动生成，请检查后使用！\n    "
                              "@task(1)\n    "
                              "def __{name}(self):\n        "
                              "self.api('{name}')\n\n".format(name=name)
                      )
        print('该方法已生成到性能测试文件下')
        WriteTestCase(filepath=test_api_path,
                      linenum=-1,
                      content="\n#该代码由工具自动生成，请检查后使用！"
                              "\n    def test{name}(self):\n"
                              "        r = self.api('{name}')\n".format(name = name)
                      )
        print('该方法已生成到接口测试文件下')


json_to_yaml(name=name,url=url,meth=meth)