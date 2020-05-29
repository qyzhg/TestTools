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
    from locust import HttpLocust, TaskSet, task, between
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






#Fri May 29 16:20:00 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __login_sheshi(self):
        self.api('login_sheshi')




#Fri May 29 16:45:57 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __licenseBusiness_asyListQuery(self):
        self.api('licenseBusiness_asyListQuery')


#Fri May 29 17:50:57 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __licenseBusiness_asyListQuery(self):
        self.api('licenseBusiness_asyListQuery')


#Fri May 29 17:57:03 2020:该代码由工具自动生成，请检查后使用！
    @task(1)
    def __licenseBusiness_asyListQuery(self):
        self.api('licenseBusiness_asyListQuery')

class Staff(HttpLocust):
    '''放到最下面'''
    task_set = VirtualUser
    wait_time = between(0.5, 3)