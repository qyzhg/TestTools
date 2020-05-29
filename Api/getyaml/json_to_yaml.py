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
import argparse
import os
import sys
import time
sys.path.append(os.path.abspath('../..'))
from Api.settings import *
from Api.WriteTestCase import WriteTestCase
from data_to_json import DataToJson

parser = argparse.ArgumentParser(description='先将需要转换的json放入json文件中 命令为python --n 接口名 --u 接口地址 --m 请求方式')
parser.add_argument('--n', type=str,help='接口名，例如：login')
parser.add_argument('--u', type=str,help='接口地址，例如：a/login')
parser.add_argument('--m', type=str,help='请求方式，只能输入三种请求方式：GET，POST/data，POST/json')

args = parser.parse_args()
#获取参数
#处理带有前缀的URL
url = args.u
if HOST in url:
    url = url.split(HOST)[1]
name = args.n
print(name)
if name == '@auto':
    name = url.replace('/','_')
    print(name)
meth = args.m
#yaml输出路径
case_path = os.path.join(CASE_DIR,name) + '.yaml'
#性能文件路径
locustfile_path = os.path.join(LOCUSTFILE_DIR, 'locustfile.py')
#接口测试文件路径
test_api_path = os.path.join(TEST_API_DIR,'test_lm_api.py')



def json_to_yaml(name,url,meth):
    u_select = input('是否需要将代码追加到文件中？\n'
                     '【1】：将文件追加到性能测试脚本文件和接口测试脚本文件中(默认)\n'
                     '【2】：将文件只追加到性能测试脚本文件中\n'
                     '【3】：将文件只追加到接口测试脚本文件中\n'
                     '【4】：仅生成yaml文件，不向测试脚本文件中追加\n')

    if u_select == '':
        u_select = 1

    try:
        u_select = int(u_select)
    except ValueError:
        print('请输入正确的选项！')
        sys.exit(0)

    if u_select>4 or u_select<1:
        print('请输入正确的选项！')
        sys.exit(0)

    #生成yaml文件
    with open('json', 'r', encoding='utf-8') as f:
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
            with open('json', 'r', encoding='utf-8') as f:
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

    if u_select == 1:
        make_locustfile(name=name)
        male_apifile(name=name)

    elif u_select == 2:
        make_locustfile(name=name)

    elif u_select == 3:
        male_apifile(name=name)


def make_locustfile(name):
    WriteTestCase(filepath=locustfile_path,
                  linenum=-4,
                  content="\n#{t}:该代码由工具自动生成，请检查后使用！\n    "
                          "@task(1)\n    "
                          "def __{name}(self):\n        "
                          "self.api('{name}')\n\n".format(name=name,t = time.ctime())
                  )
    print('该方法已生成到性能测试文件下')


def male_apifile(name):
    WriteTestCase(filepath=test_api_path,
                  linenum=-1,
                  content="\n#{t}该代码由工具自动生成，请检查后使用！"
                          "\n    def test_{name}(self):\n"
                          "        r = self.api('{name}')\n".format(name = name,t = time.ctime())
                  )
    print('该方法已生成到接口测试文件下')


json_to_yaml(name=name,url=url,meth=meth)