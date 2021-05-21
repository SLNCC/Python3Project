# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

"""一个可表示汽车的类"""
class Car(object):

    def __init__(self,make,model,year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_tank =  90



    def get_descriptive_name(self):
        """ 返回整洁的描述性信息 """
        long_name = str(self.year) + ' ' +self.make+' ' + self.model
        return  long_name.title()

    def write_odometer(self,mile):
        # """将里程表设置为指定的值"""
        # self.odometer = mile
        """将里程表读数设置为指定的值 禁止里程表读数往回调"""
        if mile >= self.odometer:
            self.odometer = mile
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,mile):
        # """将里程表读数增加指定的量"""
        if mile > 0:
         self.odometer  +=mile

    def read_odometer(self):
        """ 打印一条支出汽车里程的信息 """
        long_name = str(self.year) + ' ' +self.make+' ' + self.model

        print("This car has " +str(self.odometer)+" miles ob it")

    def fill_gas_tank(self):
        """多少L油量"""
        print("This car has " + str(self.gas_tank) + " L")


