# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import  requests,bs4

# res = requests.get('https://www.baidu.com/')
# print(res)
# res.raise_for_status()
# bdSoup = bs4.BeautifulSoup(res.text)
# print(type(bdSoup))

htmlFile = open("bd.html")

bdSoup = bs4.BeautifulSoup(htmlFile)

# 用 select()方法寻找元素
"""
  soup.select('div') 所有名为<div>的元素
soup.select('#author') 带有 id 属性为 author 的元素
soup.select('.notice') 所有使用 CSS class 属性名为 notice 的元素
soup.select('div span') 所有在<div>元素之内的<span>元素
soup.select('div > span') 所有直接在<div>元素之内的<span>元素，中间没有其他元素
soup.select('input[name]') 所有名为<input>，并有一个 name 属性，其值无所谓的元素
soup.select('input[type="button"]') 所有名为<input>，并有一个 type 属性，其值为 button 的元素
"""

# elems = bdSoup.select('p')
# # print(elems)
#
# # print(type(bdSoup))
#
# print(elems[0])
# print(elems[0].attrs)


#通过元素的属性获取数据
elems = bdSoup.select('span')[0]

# print(str(elems))

spanid = elems.get('id')
print('some_nonexistent_addr: %s'%(elems.get('some_nonexistent_addr') == None))

print('id：%s'%spanid)

print('attrs: %s'%elems.attrs)