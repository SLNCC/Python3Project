# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



import sys
import re
import collections


"""创建一个从单词到其出现情况的映射"""

WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list)

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
         for match in WORD_RE.finditer(line):
             word = match.group()
             column_no = match.start()+1
             location = (line_no, column_no)

             index[word].append(location)

 # 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])



dd = collections.defaultdict(list)
dd.get('456')
print(dd) #defaultdict(<class 'list'>, {})


dd['k'] = '123'
print(dd)  #defaultdict(<class 'list'>, {'k': '123'})


#StrKeyDict0 在查询的时候把非字符串的键转换为字符串
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise  KeyError(key)
        return  self[str(key)]

    def get(self, key,default = None):
        try:
            return self[key]
        except KeyError:
            return default
        pass

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()





d = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'])
# print(d['1'])#KeyError: '1'

print(d.get('2'))
print(d.get(4)) #None

print(d.get(1)) #None
print(d.get(None)) #None

print('2' in d)
print('1' in d)


# 下面的小例子利用 Counter 来计算单词中各个字母出现的次数：
ct = collections.Counter('abracadabra')

print(ct)
ct.update('aaaaazzzb')
print(ct)

ct.most_common(1)
print(ct)


#不可变映射类

from  types import  MappingProxyType

d= {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1]) #d 中的内容可以通过 d_proxy 看到。
# d_proxy[2] = 'x' #但是通过 d_proxy 并不能做任何修改。
"""
    Traceback (most recent call last):
                 d_proxy[2] = 'x'
    TypeError: 'mappingproxy' object does not support item assignment
"""

d[2] = 'B'
print(d)
print(d_proxy) #d_proxy 是动态的，也就是说对 d 所做的任何改动都会反馈到它上面。


