# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


from  dis import  dis


print(dis('{1}'))
print(dis('set([1])'))


print(frozenset(range(10)))
print(frozenset([1,2,3,4,5,6]))

print(type({1}) )


from unicodedata import name

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')})

# {'§', '=', '¢', '#', '¤', '<', '¥', 'μ', '×', '$', '¶', '£', '©',
# '°', '+', '÷', '±', '>', '¬', '®', '%'}