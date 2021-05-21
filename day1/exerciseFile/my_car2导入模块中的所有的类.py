# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'



#导入模块中的所有的类
from car import *
"""
不推荐使用这种导入方式，其原因有二。
首先，如果只要看一下文件开头的import 语句，就能清楚地知道程序使用了哪些类，将大有裨益;
但这种导入方式没有明确地指出你 使用了模块中的哪些类。这种导入方式还可能引发名称方面的困惑。
如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
这里之所以介绍这种导 入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。
需要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.class_name 语法来访问类。
这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知 道在程序的哪些地方使用了导入的模块;
你还避免了导入模块中的每个类可能引发的名称冲突。

"""

my_new_car = Car('audi','a+',2018)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer = 200
my_new_car.write_odometer(800)
my_new_car.read_odometer()
my_new_car.increment_odometer(200)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()


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








my_elc_car = ElectricCar("satana",'model s',2017)

electricCarInfo = my_elc_car.get_descriptive_name()


print(electricCarInfo)

my_elc_car.increment_odometer(500)
my_elc_car.read_odometer()

my_elc_car.battery.describe_barrtery()
my_elc_car.battery.get_range()
my_elc_car.fill_gas_tank()