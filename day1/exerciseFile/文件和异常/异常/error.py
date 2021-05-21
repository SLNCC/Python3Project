# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



# ZeroDivisionError: division by zero
# print(1/0)

try:
    print(1/0)
except ZeroDivisionError:
    print("you don't divide by zero")