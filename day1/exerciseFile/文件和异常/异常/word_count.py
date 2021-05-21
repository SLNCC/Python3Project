# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

def count_words(file_name):
    try:
        with open(file_name) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
        """
        1.Python有一个pass 语句，可在代码块中使用它来让Python 什么都不要做.
        2.pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么
        """

        # print("Sorry,the file: " + file_name + " does not exist")
    else:

        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words ")

#
# file_name = 'alice.txt'
# count_words(file_name)


filenames = ['alice.txt','guest.txt','programming.txt']


for filename in filenames:
    count_words(filename)