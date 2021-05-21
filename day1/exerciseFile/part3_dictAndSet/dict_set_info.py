# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from collections import abc

__author__ = 'joedd'

'''
    泛映射类型就是广义上的对应关系，在数学中，我们将集合A对应集合B中的对应法则称为"映射"（Mapping）
    同样，在python里，我们称"键值对"为映射，这其实也是一种对应法则
    如果一个数据类型是映射，那么它肯定属于collections.abc.Mapping，可使用isinstance函数测试

    PS: 字典是 Python 语言中唯一的映射类型。映射类型对象里哈希值(键) 和指向的对象(值)是一对多的关系。
'''

"""
    非抽象映射类型一般不会直接继承这些抽象基类，它们会直接对
    dict 或是 collections.User.Dict 进行扩展。
    
    这些抽象基类的主要作用是作为形式化的文档，它们定义了构建一个映射类型所需要的最
    基本的接口。
    然后它们还可以跟 isinstance 一起被用来判定某个数据是不是广义上的映射类型.
    
"""
my_dict = {}

#这里用 isinstance 而不是 type 来检查某个参数是否为 dict 类型，
# 因为这个参数有可能不是 dict，而是一个比较另类的映射类型。

print(isinstance(my_dict, abc.Mapping))

"""
    如果一个对象是可散列的，那么在这个对象的生命周期中，它
    的散列值是不变的，而且这个对象需要实现 __hash__() 方
    法。另外可散列对象还要有 __qe__() 方法，这样才能跟其
    他键做比较。如果两个可散列对象是相等的，那么它们的散列
    值一定是一样的…

"""

"""
    原子不可变数据类型（str、bytes 和数值类型）都是可散列类
    型，frozenset 也是可散列的，因为根据其定义，frozenset
    里只能容纳可散列类型。元组的话，只有当一个元组包含的所有元
    素都是可散列类型的情况下，它才是可散列的。

"""

tt = (1,2,(30,40))
print(hash(tt)) #True

tl = (1, 2, [30, 40])

# print(hash(tl)) #TypeError: unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))

print(hash(tf))


a = dict(one=1, two=2, three=3)

print(a)
b = {'one': 1, 'two': 2, 'three': 3}

print(b)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)

d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)

e = dict({'three': 3, 'one': 1, 'two': 2})
print(e)

print(a==b==c==d==e)
