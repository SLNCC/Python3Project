# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'




while True:

    first_number = input("Please input a number: ")

    sec_number = input("Please input once number: ")


    try:
        result = int(first_number) + int(sec_number)

    except :
         print("input var type error !!!")

    else:
        print("计算的结果是：" + str(result))
