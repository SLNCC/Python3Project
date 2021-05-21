# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


"""
处理FileNotFoundError 异常
"""

filename = 'alice.txt'

#FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

