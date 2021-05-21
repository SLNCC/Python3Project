# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from numpy import sort

__author__ = 'joedd'




print("hello",end='')
print(" world")


# def spam():
#    eggs = 31337
#
# spam()
# print(eggs)




# def spam(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error:Invalid argument')
#
# print(spam(0))
#
# print(spam(2))


import  random


# secret = random.randint(1,20)
# print('I am thinking of a number betweeen 1 and 20.')
#
# for guessesTaken in  range(1,7):
#     print('Take a guess.')
#     guess = int(input())
#     if guess < secret:
#         print('Your guess is too low')
#     elif guess > secret:
#         print('Your guess is too high')
#     else:
#         print('This condition is the correct guess!')
#         break
#
#     if guess == secret:
#         print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
#     else:
#         print('Nope. The number I was thinking of was ' + str(secret))


# spams= [1,2,3,4,5,6]
# print(spams)
#
# print(1 in spams)

#多重赋值技巧：变量的数目和列表的长度必须严格相等，否则 Python 将给出 ValueError。
# cat = ['fat','black','loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# size,color,disposition = cat
#
# print(size,color,disposition)


#增强赋值
# spam = 22;
# # spam += 1
# # spam -=1
# # spam/=1
# # spam//=3
# spam %= 4
# print(spam)

# 用 index()方法在列表中查找值--找到并返回下标

# spam = ['hello','hi','howdy','hedian'];


# print(spam.index('hello'))
#insert() takes exactly 2 arguments
#方法属于单个数据类型。append()和 insert()方法是列表方法，只能在列表上调
# 用，不能在其他值上调用，例如字符串和整型。
# spam.insert(0,'world')
#
# print(spam)
# spam.append('hello2')
# print(spam)
#
# #直接删除值
# # spam.remove('hello2')
# #用下标删除
# del spam[-1]
# print(spam)

# eggs = 'hello'
#
# eggs.append('world')
# print(eggs)

"""
  1.sort()方法当场对列表排序。不要写出 spam = spam.sort()这样的代码，试图记录返回值。
  2.不能对既有数字又有字符串值的列表排序，因为 Python 不知道如何比较它们。
     在交互式环境中输入以下代码spam = [2,10,2.5,7,3.6,1.5,'a'];，注意 TypeError 错误
"""
# spam = [2,10,2.5,7,3.6,1.5];
#
# spam.sort(reverse=True)
#
# print(spam)
# import random
# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definitely',
#             'Reply hazy try again',
#             'Ask again later',
#             'Concentrate and ask again',
#             'My reply is no',
#             'Outlook not so good',
#             'Very doubtful']
# print(messages[random.randint(0, len(messages) - 1)])


# name = 'qiao dd'
#
#
# # for i in name:
# #     print(' * * * ' + i + ' * * * ')
#
# new_name = name[0:4] + '+' + name[5:7]
# print(new_name)

# eggs = [1, 2, 3]
#这里 eggs 中的列表值并没有改变，而是整个新的不同的列表值([4, 5, 6])，覆写了老的列表值
# eggs = [4, 5, 6]

# print(eggs)

#要确实要修改eggs中原来的列表

# del  eggs[2]
# del  eggs[1]
# del  eggs[0]
#
# eggs.append(4)
# eggs.append(5)
#
# eggs.append(6)
#
# print(eggs)



#元组
"""
但元组与列表的主要区别还在于，元组像字符串一样，是不可变的。
元组不能让它们的值被修改、添加或删除。

"""

# eggs = ('hello',1,2,3)
# print(eggs)

#TypeError: 'tuple' object does not support item assignment
# eggs[0] = 0

# 2.如果元组中只有一个值，你可以在括号内该值的后面跟上一个逗号，表明这种
# 情况。
#Python 可以实现一些优化，让使用元组的代码比使用列表的代码更快。
#
# print(type(('hello')))
# print(type(('hello',)))


# 3.用 list()和 tuple()函数来转换类型

"""
    在变量必须保存可变数据类型的值时，
    例如列表或字典，Python 就使用引用。
    对于不可变的数据类型的值，
    例如字符串、整型或元组，Python变量就保存值本身。

"""

# tuple_arr = tuple([1,2,3,4,5])
#
# print(tuple_arr)
#
# list_arr = list(tuple_arr)
#
# print(list_arr)

# 4.当你将列表赋给一个变量时，实际上是将列表的“引用”赋给了该变量。
# 引用是一个值，指向某些数据。列表引用是指向一个列表的值。

# spam = [0,1,2,3,4,5,6]
# cheese = spam
#
# cheese[1] = 'hello'
#
# print(spam)
# print(cheese)

#5.copy 模块的 copy()和 deepcopy()函数

"""
   copy()可以用来复制列表或字典这样的可变值，而不只是复制引用
   
   如果要复制的列表中包含了列表，那就使用 copy.deepcopy()函数来代替。
    deepcopy()函数将同时复制它们内部的列表。
"""
import copy
# spam = [0,1,2,3,4,5,6]
# #
# # cheese = copy.copy(spam)#创建了第二个列表，能独立于第一个列表修改
# #
# # cheese[1] = 'hello'
# #
# # print(spam)
# # print(cheese)

# spam = [0,1,2,3,4,5,6]
#
# cheese = copy.deepcopy(spam)
#
# cheese[1] = 'hello'
#
# print(spam)
# print(cheese)


#6.字-典

"""
   因为 dic 字典中没有'c'键，get()方法返回的默认值是 None。不使用 get()，
代码就会产生一个错误消息

"""

# dic = {"a":1,"b":2}

"""
   print(dic['c'])
KeyError: 'c'
print(dic['c'])
"""
# print(dic.get('c'))
# print(dic.get('c',0))


# 5.1 setdefault()方法

"""

    setdefault()方法提供了一种方式，在一行中完成这件事。传递给该方法的第一
    个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。如果该键
    确实存在，方法就会返回键的值

"""

# spam = {'name': 'Pooka', 'age': 5}
# # if 'color' not in spam:
# #     spam['color'] = 'black'
# spam.setdefault('color','white')
# #可以确保一个键存在
# spam.setdefault('color','black')
#
# print(spam)

#7.漂亮打印
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
#     # print(count)
#     pprint.pprint(count)



arr = [2,5,6,1,0,10,7]
# sort(arr) 返回一个copy of Arr
#TypeError: sort() got an unexpected keyword argument 'reverse'
# print(sort(arr,reverse=True))
print(sort(arr))

#sorted() 默认返回一个升序的新建列表
print(sorted(arr,reverse=True))