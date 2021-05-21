# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'





class User:

    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.login_attempts = 0

    def increment_login_attempts(self,login_attemps):
        """加1操作"""
        if login_attemps > 0:
            self.login_attempts = login_attemps

    def reset_login_attempts(self):
        """重置为0"""
        self.login_attempts = 0



    def describe_user(self):
        print("User's name : " +str(self.first_name) + str(self.second_name)+".")
        print("User's login_attempts : " + str(self.login_attempts) + ".")

    def greet_user(self):
        print("你好, " + str(self.first_name) + self.second_name.title()+"!!!")



one_user =  User("qiao","dd")
one_user.describe_user()
one_user.greet_user()

one_user.increment_login_attempts(100)
one_user.describe_user()

