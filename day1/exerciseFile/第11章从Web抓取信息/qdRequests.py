# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import requests

# 一、requests.get(）函数下载一个页面
# res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# print(res)            #  1.返回结果：   <Response [200]>

#print(type(res))       #2.打印的结果：类型为：  <class 'requests.models.Response'>

# print(res.status_code)  # 3.网络状态码： 200  404 状态码：404 Client Error: Not Found for url

# print(res.text)         # 4.打印文本

# print(res.text[:250])         # 5.输出 1-249字符（显示前 250 个字符）



#



#  二、检查错误

"""
   raise_for_status()方法是一种很好的方式，确保程序在下载失败时停止。
     1）、程序在发生未预期的错误时，马上停止。
     2）、如果下载失败对程序来说不够严重，
         可以用 try 和 except 语句将 raise_for_status()代码行包裹起来，
         处理这一错误，不让程序崩溃。
"""

#1.错误的url.报异常

# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

#2.正确的url.

# res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# try:
#     res.raise_for_status()
#
#     # print( res.status_code())
# except Exception as exc:
#     print('异常错误信息：%s'%exc)



"""
  3.将下载的文件保存到硬盘
  
    1.用标准的 open()函数和 write():('wb)方法
    2.写入二进制数据而不是文本数据,的是为了保存该文本中的“Unicode 编码”。
  
   下载并保存到文件的完整过程如下：
        1．调用 requests.get()下载该文件。
        2．用'wb'调用 open()，以写二进制的方式打开一个新文件。
        3．利用 Respose 对象的 iter_content()方法做循环。
        4．在每次迭代中调用 write()，将内容写入该文件。
        5．调用 close()关闭该文件。

"""

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print(res.raise_for_status())
playFile = open('RemeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    # playFile.write(chunk)  #write()方法返回一个数字，表示写入文件的字节数
    print( playFile.write(chunk))
    # print(len(chunk))

playFile.close()

