# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


file_name = 'pi_digits.txt'
with open(file_name)  as file_obj:
    contents = file_obj.read()
    print('\n' + contents.rstrip() + '\n') #Python方法rstrip() 删除(剥除)字符串末尾的空白

file_name1 = '../python_work/file_name.txt'
with open(file_name1)  as file_obj:
    contents = file_obj.read()
    print('\n' + contents.rstrip() + '\n') #Python方法rstrip() 删除(剥除)字符串末尾的空白


