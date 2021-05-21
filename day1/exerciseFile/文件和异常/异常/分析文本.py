# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


# title = "my name is qiao dd"
#
#
# print(title.split())



file_name = "alice.txt"

try:
    with open(file_name) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:

    print("Sorry,the file: " + file_name + "does not exist")
else:

    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " +str(num_words) + " words " )

