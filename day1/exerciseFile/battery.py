# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



#定义一个电池实类

class  Battery(object):
    "电动车汽车电瓶"
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_barrtery(self):
        """打印一条描述电瓶容量的信息"""
        print("This Car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)