# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import  json

"""
   dump():存储数据
   load():读取数据
"""

numbers = [1,2,3,4,5,6,7,8]

filename = 'number.json'

with open(filename,'w') as file_obj:
    json.dump(numbers,file_obj)