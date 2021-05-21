# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



class Restaurant:
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant's name is "+self.restaurant_name.title() + ".")
        print("Restaurant's type is " + str(self.restaurant_type) + ".")

    def open_restaurant(self):
        print("餐馆正在营业")

    def set_number_served(self,persons):
        """设置就餐的人数"""

        if persons > 0:
            self.number_served = persons
            print("设置就餐人数：" + str( self.number_served ))


    def increment_number_served(self, persons):
        """设置就餐的人数"""
        if persons > 0:
            self.number_served += persons
            print("就餐的总数人数：" + str(self.number_served))




restaurant_ins = Restaurant("中华一条街餐馆","十里飘香")

# print(restaurant_ins.restaurant_name)
# print(restaurant_ins.restaurant_type)

restaurant_ins.open_restaurant()
restaurant_ins.set_number_served(100)
restaurant_ins = Restaurant("中华老字号","万里飘香")
restaurant_ins.describe_restaurant()
restaurant_ins.increment_number_served(300)



#
# restaurant_ins2 = Restaurant("中华第一香","飘香随来")
# restaurant_ins2.describe_restaurant()
# restaurant_ins2.open_restaurant()
