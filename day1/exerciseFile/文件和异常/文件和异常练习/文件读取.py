# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from nis import cat

__author__ = 'joedd'



first_file = "cats.txt"

sec_file = "dogs.txt"



def read_file(type):
    file_name = type + ".txt"
    try:
       with open(file_name) as file_obj:
            contents = file_obj.readlines()
    except FileNotFoundError:
        pass
        """
        1.Python有一个pass 语句，可在代码块中使用它来让Python 什么都不要做.
        2.pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么
        """

        # print("Sorry,the file: " + file_name +".txt" + " does not exist")
    else:


        print("The file " + file_name +".txt "+ " has  " + str(len(contents)) +" "+ type)

def write_file(type):
    file_name = type + ".txt"
    i =0
    while i <3:
        name = input("please input name:")

        if len(name) >0 :
            with open(file_name, 'a') as file_obj:
                file_obj.write(name + '\n')
                i = i + 1
                print("添加" + str(i))
        else:
            print(" content is not an empty string")


while True:
    type = input("please input type:")

    # write_file(type)
    read_file(type)




