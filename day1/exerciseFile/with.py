# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

# 为了避免打开文件后忘记关闭，可以通过管理上下文，即：
#
# with open('log', 'r') as f:
#     ...
# 如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。
#
# 在Python  2.7 后，with又支持同时对多个文件的上下文进行管理，即：
#
# with open('log1') as obj1, open('log2') as obj2:
#     pass


# with open('lyrics.rtf') as f:
#     data = f.read()
#     print('打印数据：\n'+data)


with open('lyrics.rtf') as f,open('lyrics.rtf') as f1:
    data = f.read()
    data1 = f1.read()
    print('打印数据：\n' + data +'\n\n打印数据2：\n'+data1)
