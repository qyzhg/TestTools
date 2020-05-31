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
    def on_start(self) -> None:
        '''
        -初始化方法
        -将需要的类在此方法中实例化
        :return:None
        '''
        self.s = self.client
        Api.__init__(self,self.s)



class Staff(HttpLocust):
    '''放到最下面'''
    task_set = VirtualUser
    wait_time = between(0.5, 3)