# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

#逐行读取
file_name = 'pi_digits.txt'
# with open(file_name)  as file_obj:
#     # contents = file_obj.read()
#     # print('\n' + contents.rstrip() + '\n') #Python方法rstrip() 删除(剥除)字符串末尾的空白
#
#     for line in file_obj:
#         print(line.rstrip())

with open(file_name)  as file_obj:
    lines = file_obj.readlines()  #方法readlines() 从文件中读取每一行，并将其存储在一个列表中



print(lines )
for line in lines:
    print(line.rstrip())




file_name1 = '../python_work/file_name.txt'
with open(file_name1)  as file_obj:
    contents = file_obj.read()
    print('\n' + contents.rstrip() + '\n') #Python方法rstrip() 删除(剥除)字符串末尾的空白


