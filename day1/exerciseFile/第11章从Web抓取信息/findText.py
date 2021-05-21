# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import requests

"""

从命令行参数中获取查询关键字。
    • 取得查询结果页面。
    • 为每个结果打开一个浏览器选项卡。
这意味着代码需要完成以下工作：
    • 从 sys.argv 中读取命令行参数。
    • 用 requests 模块取得查询结果页面。
    • 找到每个查询结果的链接。
    • 调用 webbrowser.open()函数打开 Web 浏览器。
"""



import requests, sys, webbrowser, bs4


# 1. 从 sys.argv 中读取命令行参数,用 requests 模块取得查询结果页面。

print('Googling...') # display text while downloading the Google page

# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.baidu.com?' + ' '.join(sys.argv[1:]))


res.raise_for_status()
print(res.status_code)

# 2. 找到每个查询结果的链接。
soup = bs4.BeautifulSoup(res.text)
print(soup)
# 所有具有 CSS 类 bri 的元素中的<a>元素，但是有问题
linkElems = soup.select('a')
print(linkElems)

# 3. 调用 webbrowser.open()函数打开 Web 浏览器。
numOpen = min(10,len(linkElems))

for  i in range(numOpen):
    # 'http://google.com' +
    webbrowser.open(linkElems[i].get('href'))
    print('------------')