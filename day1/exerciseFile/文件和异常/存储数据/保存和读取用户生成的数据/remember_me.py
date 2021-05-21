# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import  json



# filename = "username.json"
#
# # with open(filename ,'w') as file_obj:
# #      json.dump(name,file_obj)
# #      print("We will remember you when you come bcak,"+name +'!!')
#
# try:
#     with open(filename) as file_obj:
#         username = json.load(file_obj)
# except FileNotFoundError:
#     username = input("Please input username :")
#     with open(filename,'w') as file_obj:
#          json.dump(username,file_obj)
#          print("We will remember you when you come bcak," + username + '!!')
# else:
#     print("Welcome back," + username + '!!!')



# def greet_user():
#     """问候用户，并指出其名字"""
#     filename = "username.json"
#     try:
#         with open(filename) as file_obj:
#             username = json.load(file_obj)
#     except FileNotFoundError:
#         username = input("Please input username :")
#         with open(filename,'w') as file_obj:
#              json.dump(username,file_obj)
#              print("We will remember you when you come bcak," + username + '!!')
#     else:
#         print("Welcome back," + username + '!!!')
#
#
# greet_user()


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as file_obj:
            try:
                username = json.load(file_obj)
                print(username)
            except  :
                return  None
    except FileNotFoundError:
        return  None
    else:
        return  username

def get_new_username():
    """提示用户输入名字"""
    filename = "username.json"
    username = input("Please input username :")
    filename = "username.json"
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back," + username + '!!!')
    else:
        username = get_new_username()
        print("We will remember you when you come back," + username + '!!')


greet_user()

