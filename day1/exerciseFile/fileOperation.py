
# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# 对文件操作流程
#
#  1.打开文件，得到文件句柄并赋值给一个变量
#  2.通过句柄对文件进行操作
#  3.关闭文件

f = open('lyrics.rtf')

first_line = f.readline()
#读一行
print('first_line:\n' +first_line)
print('分割线'.center(50,'-'))
#读取剩下的所有内容，文件大时不要用
data = f.read()
print(data)

f.close()





# 打开文件的模式有：
#
# r，只读模式（默认）。
# w，只写模式。【不可读；不存在则创建；存在则删除内容；】
# a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
# "+" 表示可以同时读写某个文件
#
# r+，可读写文件。【可读；可写；可追加】
# w+，写读
# a+，同a
# "U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）
#
# rU
# r+U
# "b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
#
# rb
# wb
# ab