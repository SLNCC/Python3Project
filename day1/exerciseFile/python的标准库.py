# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


# from collections import  OrderedDict

from  random import  randint


import collections


x = randint(1,100)

print("range:" + str(x))






dict = collections.OrderedDict()

dict['name'] = "qiaodd"

dict['age'] = "我不想说"

dict['sex'] = "M"

for key,value in dict.items():
    print("key_name: " + str(key) +'      ,' + "key_value: " + str(value)+" .")
