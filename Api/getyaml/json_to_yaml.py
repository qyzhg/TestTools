#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   测试yaml.py
 
@Time    :   2020/5/26 10:39 上午
'''
try:
    import ruamel.yaml
except ImportError:
    print('发现缺少的依赖库，工具正在尝试安装，如安装失败，请使用pip install ruamel.yaml命令自行安装')
    import os
    os.system('pip install ruamel.yaml')
    import ruamel.yaml
import ast
import os
import sys
import time
sys.path.append(os.path.abspath('../..'))
from Api.settings import *
from Api.public.WriteTestCase import WriteTestCase
from Api.getyaml.data_to_json import DataToJson


def json_to_yaml(name,url,meth,case_path):
    '''
    将json文件中的文件转换生成yaml格式的测试用例
    :param name: 接口名
    :param url:
    :param meth:
    :param case_path:
    :return:
    '''
    meth = meth.upper()
    if 'JSON' not in meth and 'DATA' not in meth and 'GET' not in meth:
        print('meth参数输入有误，请使用--help参数查看帮助')
        sys.exit(0)
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        try:
            dict_f = ast.literal_eval(str(f.read()))
            dict_var = {
                        'name':name,
                        'url':url,
                        'meth':meth,
                        'params':
                            dict_f
                        }
        except:
            DataToJson()
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                dict_f = ast.literal_eval(str(f.read()))
                dict_var = {
                    'name': name,
                    'url': url,
                    'meth': meth,
                    'params':
                        dict_f
                }

    with open(case_path,'w+',encoding='utf-8') as case_file:
        print(ruamel.yaml.dump(dict_var,Dumper=ruamel.yaml.RoundTripDumper,allow_unicode=True),file=case_file)
        print('已生成接口配置文件：'+case_path)


def make_locustfile(name):
    WriteTestCase(filepath = LOCUSTFILE_FILE,
                  linenum = -4,
                  content = "\n#{t}:该代码由工具自动生成，请检查后使用！\n    "
                          "@task(1)\n    "
                          "def __{name}(self):\n        "
                          "self.api('{name}')\n\n".format(name=name,t = time.ctime())
                  )
    print('该方法已生成到性能测试文件下')


def make_apifile(name):
    WriteTestCase(filepath=TEST_API_FILE,
                  linenum=-1,
                  content="\n#{t}该代码由工具自动生成，请检查后使用！"
                          "\n    def test_{name}(self):\n"
                          "        r = self.api('{name}')\n".format(name = name,t = time.ctime())
                  )
    print('该方法已生成到接口测试文件下')