# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import webbrowser, sys, pyperclip

"""
  写一个简单的脚本，利用剪贴板中的内容在浏
览器中自动加载地图

1.从命令行参数或剪贴板中取得街道地址。
2.打开 Web 浏览器，指向该地址的 Google 地图页面。

这意味着代码需要做下列事情：
    1)从 sys.argv 读取命令行参数。
    2)读取剪贴板内容。
    3)调用 webbrowser.open()函数打开外部浏览器。
"""

if len(sys.argv) > 1:
    # Get address from command line.
    """
        2.命令行参数通常用空格分隔
          使用sys.argv[1:]，砍掉这个数组的第一个元素
    """

    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # 3.处理剪贴板内容，加载浏览器
    address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)



"""
    手工取得地图                          利用 mapIt.py
    
    高亮标记地址                           高亮标记地址
    拷贝地址                               拷贝地址
    
    打开 Web 浏览器                       运行 mapIt.py
    打开 http://maps.google.com/
    点击地址文本字段
    拷贝地址
    按回车

"""
"""
  4.类似程序的想法
  
            只要你有一个 URL，webbrowser 模块就让用户不必打开浏览器，而直接加载一
            个网站。
            其他程序可以利用这项功能完成以下任务：
                • 在独立的浏览器标签中，打开一个页面中的所有链接。
                • 用浏览器打开本地天气的 URL。
                • 打开你经常查看的几个社交网站。
"""
# webbrowser.open('https://www.baidu.com')



