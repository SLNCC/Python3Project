# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



"""

调用open() 时提供了两个实参。
第一个实参也是要打开的文件的名称；
第二个实参（'w' ）告诉Python，我们要以写入模式 打开这个文件。
打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。
如果你省略了模式实参，Python将以默认的只读模式打开文件。
如果你要写入的文件不存在，函数open() 将自动创建它。然而，以写入（'w' ）模式打开文件时千万要小心，
因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。

"""
# filename = 'programming.txt'
#写文件
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming." + '\n')
#     file_object.write("I love creating new games." + '\n')

#附加文件--添加到文件的末尾
# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")

filename = 'guest.txt'




# name = input("please input name:")
#
#
# with open(filename,'w') as file_obj:
#
#     file_obj.write(name)


# while 1:
#     name = input("please input name:")
#
#     with open(filename,'a') as file_obj:
#
#         file_obj.write(name + '\n')
#         print("谢谢配合工作，您已签到")


# while 1:
#     name = input("您为何喜欢编程:")
#
#     with open(filename,'a') as file_obj:
#
#         file_obj.write(name + '\n')


