#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   locustfile.py
 
@Time    :   2020/5/28 11:06 上午
'''

import os,sys
try:
    from locust import HttpLocust,TaskSet,task,between
except ImportError:
    print('发现缺少的依赖库，正在尝试安装，如果安装失败，请使用pip install locust命令自行安装')
    os.system('pip install locust')
sys.path.append(os.path.abspath('../..'))
from Api.API import Api



class VirtualUser(TaskSet,Api):
    '''
    虚拟用户类
    '''
    def on_start(self):
        '''
        -初始化方法
        -将需要的类在此方法中实例化
        :return:
        '''
        self.s = self.client
        Api.__init__(self,self.s)





#该代码由工具自动生成，请检查后使用！
    @task(1)
    def __test(self):
        self.api('test')


#该代码由工具自动生成，请检查后使用！
    @task(1)
    def __testname(self):
        self.api('testname')


#Thu May 28 21:35:42 2020该代码由工具自动生成，请检查后使用！
    @task(1)
    def __testname(self):
        self.api('testname')


#Thu May 28 21:36:12 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __testname(self):
        self.api('testname')


#Thu May 28 21:36:54 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __testname(self):
        self.api('testname')

class Staff(HttpLocust):
    '''放到最下面'''
    task_set = VirtualUser
    wait_time = between(0.5, 3)