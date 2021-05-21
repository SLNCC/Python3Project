# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



# def isPhoneNumber(text):
# #
# #     if len(text) != 12:
# #         return False
# #     for i in range(0,3):
# #         if not  text[i].isdecimal():
# #             return False
# #     if text[3] != '-':
# #         return  False
# #
# #     for i in range(4,7):
# #         if not  text[i].isdecimal():
# #             return False
# #     if text[7] != '-':
# #         return False
# #
# #     for i in range(8, 12):
# #         if not text[i].isdecimal():
# #             return False
# #
# #     return True
# #
# #
# # print('415-555-4242 is a phone number:')
# # print(isPhoneNumber('415-555-4242'))
# # print('Moshi 123is a phone number:')
# # print(isPhoneNumber('Moshi 123'))



#Python 中所有正则表达式的函数都在 re 模块中


"""
    虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
    1．用 import re 导入正则表达式模块。
    2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
    3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
    4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。
"""

import  re

 # '\d\d\d-\d\d\d-\d\d\d\d'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#
mo = phoneNumRegex.search('My number is 415-555-4242.')#会返回一个 Match 对象
print('Phone number found: ' + mo.group())
print('Phone number found: ' + mo.group(0))

print('Phone number found: ' + mo.group(1))
print('Phone number found: ' + mo.group(2))

"""
  1.向 group()方法传入 0 或不传入参数，将返回整个匹配的文本
  2.正则表达式字符串中的第一对括号是第 1 组。第二对括号是第 2 组。
  3.向 group()匹配对象方法传入整数 1 或 2，就可以取得匹配文本的不同部分。

"""

#2.用管道匹配多个分组  字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。


# heroRegex = re.compile(r'joedd|ypl|zyx')
# mo1 = heroRegex.search('joeddand ypl')
#
# print(mo1.group())
#
# mo2 = heroRegex.search('ypl and joedd')
# print(mo2.group())
#
# heroRegex = re.compile(r'joedd(lihua|ypl|zyx)')
# mo1 = heroRegex.search('joeddzyx ypl')
#
# print(mo1.group())
#
# print(mo1.group(1))



#3.用问号实现可选匹配


# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
#
# print(mo1.group())
# mo2 = batRegex.search('The Adventures of Batwoman')
#
# print(mo2.group())

"""
结果分析：
正则表达式中的(wo)?部分表明，模式 wo 是可选的分组。
该正则表达式匹配的文本中，wo 将出现零次或一次。
这就是为什么正则表达式既匹配'Batwoman'，又匹配'Batman'。

总结：1.匹配这个问号之前的分组零次或一次
     2.要匹配真正的问号字符，就使用转义字符\?
"""

# phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')#会返回一个 Match 对象
# mo2 = phoneNumRegex.search('My number is 555-4242.')#会返回一个 Match 对象
#
# print('Phone number found: ' + mo.group())
# print('Phone number found: ' + mo2.group())


#4.用星号匹配零次或多次
"""
   *（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。
   它可以完全不存在，或一次又一次地重复
"""
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
#
# print(mo1.group())
# mo2 = batRegex.search('The Adventures of Batwoman')
#
# print(mo2.group())
#
#
# mo3 = batRegex.search('The Adventures of Batwowowoman')
#
# print(mo3.group())


#4.用加号匹配一次或多次
"""
   *意味着“匹配零次或多次”，+（加号）则意味着“匹配一次或多次”。
   星号不要求分组出现在匹配的字符串中，
   但加号不同，加号前面的分组必须“至少出现一次”。
   这不是可选的。
"""
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batman')
#
# print(mo1)
#
# mo2 = batRegex.search('The Adventures of Batwoman')
#
# print(mo2.group())
#
#
# mo3 = batRegex.search('The Adventures of Batwowowoman')
#
# print(mo3.group())


#5.用花括号匹配特定次数

"""  
  如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括
号包围的数字。
"""

# haRegex = re.compile(r'(Ha){3}')

#6.贪心匹配：它们会尽可能匹配最长的字符串--默认

"""
  Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽
可能匹配最长的字符串。花括号的“非贪心”版本匹配尽可能最短的字符串，即在
结束的花括号后跟着一个问号。
"""
haRegex = re.compile(r'(Ha){3,5}')

mo1 = haRegex.search('HaHaHa')

print(mo1.group())

mo2 = haRegex.search('HaHaHaHa')

print(mo2.group())

#非贪心匹配：尽可能最短的字符串，即在结束的花括号后跟着一个问号。
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo3 = nongreedyHaRegex.search('HaHaHa')

print(mo3.group())

mo4 = nongreedyHaRegex.search('HaHaHaHa')

print(mo4.group())




#7.findall()方法和search()方法区别
"""
 1. search()将返回一个Match对象，包含被查找字符串中的“第一次”匹配的文本
 2.findall()方法将返回一组字符串，包含被查找字符串中的所有匹配。
"""

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())


mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

print(mo1) #(返回字符串的列表)

#如果有分组，则返回元组的列表

tupleNumRegx = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo2 = tupleNumRegx.findall('Cell: 415-555-9999 Work: 212-555-0000')


print(mo2) #(返回元组的列表)


#8.字符分类

"""
  缩写字符分类       表示

    \d          0 到 9 的任何数字
    
    \D          除 0 到 9 的数字以外的任何字符

    \w          任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
    
    \W          除字母、数字和下划线以外的任何字符
    
    \s          空格、制表符或换行符（可以认为是匹配“空白”字符）
    
    \S          除空格、制表符和换行符以外的任何字符

"""

xmasRegex = re.compile(r'\d+\s\w+')
""" 
    则表达式：\d+\s\w+ 匹配的文本有一个或者多个数字(\d)，
    接下来是一个空白字符(\s)，
    接下来是一个或者多个字母/数字/下划线字符（w+）
 """
xmas=  xmasRegex.findall('12 drummers, 11 pipers, 10 lords,'
                  ' 9 ladies, 8 maids, 7swans, 6 geese, '
                  '5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(xmas)


#9.建立自己的字符分类

"""
    1.通过在字符分类的左方括号后加上一个插入字符（^），就可以得到“非字符类”。
    2.非字符类将匹配不在这个字符类中的所有字符。

"""

vowelRegex = re.compile(r'[^aeiouAEIOU]')
movowel = vowelRegex.findall('RoboCop eats baby food. BABY FOOD. III')


print(movowel)





