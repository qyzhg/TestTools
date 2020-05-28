#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   mk_data.py
 
@Time    :   2020/5/28 3:25 下午
'''


from Api.API import Api
import requests

class MakeData(Api):
    def __init__(self):
        self.s = requests.Session()
        Api.__init__(self,self.s)

    def test(self):
        r = self.api('test')
        print(r)
if __name__ == '__main__':
    count = 1
    for _ in range(10000):
        MakeData().test()
        print(count)
        count += 1