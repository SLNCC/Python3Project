# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

from  car import Car

from battery import Battery

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性,再初始化电动汽车特有的属性"""
        # super(ElectricCar, self).__init__(make,model,year)
        super().__init__(make,model,year)
        #super() 是一个特殊函数，帮助Python将父类和子类关联起来
        self.battery = Battery(85)

    # def describe_barrtery(self):
    #     """打印一条描述点评容量的信息"""
    #     self.battery.describe_barrtery()
        # print("This Car has a " + str(self.battery_size) +"-kWh battery")

    #重写父类的方法--电动车加油不合适。
    def fill_gas_tank(self):
        """电动汽车不需要油"""
        print("This car doesn't need a gas tank!!!")