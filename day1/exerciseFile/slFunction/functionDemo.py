# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


# 5.1　把函数视作对象

def factorial(n):
    '''returns n!'''
    """ IndentationError: unexpected indent
       .对于此错误，最常见的原因是,没有对齐。

    """

    return (1 if n < 2 else n * factorial(n - 1))


print(factorial(42))

print(factorial.__doc__)  # returns n!  --------：  __doc__ 属性用于生成对象的帮助文本

print(type(factorial))  # <class 'function'>

fact = factorial

print(fact)  # <function factorial at 0x10e11cae8>

print(fact(5))

print(map(factorial, range(11)))

print(list(map(factorial, range(11))))


# 5.2高级函数:接受函数为参数，或者把函数作为结果返回的函数


















