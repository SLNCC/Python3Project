# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import sys
import re


"""创建一个从单词到其出现情况的映射"""

WORD_RE = re.compile(r'\w+')
index = {}

with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
         for match in WORD_RE.finditer(line):
             word = match.group()
             column_no = match.start()+1
             location = (line_no, column_no)

             # 这其实是一种很不好的实现，这样写只是为了证明论点
             # occurrences = index.get(word, [])
             # occurrences.append(location)
             # index[word] = occurrences

             # index.setdefault(word, []).append(location)
             if word not in index:
                 index[word] = []
                 index[word].append(location)

 # 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])


 # 以字母顺序打印出结果

# print('1'.join('423'))
# dic = {'hello':1,'good':2,'boy':3,'doiido':4}
# print('@'.join(dic))
#
# list_1 = ['hello','good','boy','doiido']
# print(''.join(list_1))
#
#
#
# list_2 = ('hello','good','boy','doiido',1,3)
#
# print(list_2)
#
# list_3 = [1,2,3,4,5,6]
# print(''.join(list_3)) #TypeError: sequence item 0: expected str instance, int found


