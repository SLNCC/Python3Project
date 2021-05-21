# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


file_name = 'pi_digits.txt'

#计算一下文本中圆周率的位数

with open(file_name)  as file_obj:
    lines = file_obj.readlines()  #方法readlines() 从文件中读取每一行，并将其存储在一个列表中



print(lines)


pi_string = ''

for line in  lines:
    pi_string += line.rstrip()


print(pi_string)
print(len(pi_string))



file_name_1 = 'pi_million_digits.txt'

with open(file_name_1) as file_obj:
    lines = file_obj.readlines()


pi_string = ''

for line in lines:
    pi_string += line.strip()


print(pi_string[:52]+"...")

print(len(pi_string))

birthday = input("Enter your birthday,in the form mmddyy:")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")









