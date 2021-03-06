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

try:
    import yaml
except ModuleNotFoundError:
    os.system('pip install pyyaml')

from Api.getyaml.json_to_yaml import make_locustfile, make_apifile
from Api.settings import PROJECT_NAME, CASE_DIR, HOST


def create_script(project_name):
    project_name = project_name.upper()

    if project_name == PROJECT_NAME:
        try:
            case_list = os.listdir(CASE_DIR)
        except FileNotFoundError:
            print('项目还没有创建！请使用 -start 命令创建项目，--help参考帮助')
            sys.exit(0)

        yaml_list = list(filter(lambda x: x[-5:].upper() == '.YAML', case_list))

        if yaml_list:
            # 处理文件后缀名
            cut_list = lambda x: x.upper().split('.YAML')[0]

            new_list = list()
            for _ in yaml_list:
                new_list.append(cut_list(_))

            # #存放文件对应的备注名称
            # d = dict()
            # for _ in new_list:
            #     d[_] = (get_remark(_))

            while True:
                print('请选择生成脚本的类型：\n'
                      '【1】性能脚本和接口脚本同时生成（默认）\n'
                      '【2】仅生成性能脚本\n'
                      '【3】仅生成接口脚本\n'
                      '【q】quit 退出\n'
                      )
                a = input('请输入功能编号：\n')

                if a == '1' or a == '':
                    list(map(__make_locustfile, new_list))
                    list(map(__make_apifile, new_list))
                    break

                elif a == '2':
                    list(map(__make_locustfile, new_list))
                    break

                elif a == '3':
                    list(map(__make_apifile, new_list))
                    break

                elif a.upper() == 'Q' or a == 'QUIT':
                    sys.exit(0)

                else:
                    print('选择有误，请重新选择！')


        else:
            print('测试用例文件夹没有测试用例，请检查{case_dir}'.format(case_dir=CASE_DIR))

    else:
        print('当前输入项目名称与配置文件中的项目名称不符，请检查Api>settings.py文件中的PROJECT参数')


def get_remark(file_name):
    if file_name[-5:].upper() != '.YAML':
        file_name = file_name + '.yaml'
    else:
        file_name = file_name
    with open(os.path.join(CASE_DIR, file_name), 'r', encoding='utf-8') as f:
        y = yaml.load(f.read(), Loader=yaml.FullLoader)
    # 获取yaml文件的参数
    remark = y.get('remark')
    return remark


def __make_locustfile(name):
    '''
    烂方法，临时救火用后期优化进map
    :param name:
    :return:
    '''
    remark = get_remark(name)
    make_locustfile(name=name, remark=remark)


def __make_apifile(name):
    '''
    烂的一批
    :param name:
    :return:
    '''
    remark = get_remark(name)
    make_apifile(name=name, remark=remark)


if __name__ == '__main__':
    create_script('TEST_LOCUST')
