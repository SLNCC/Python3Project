# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

#不同类做不同的事情

# from  electricCar import  ElectricCar,Car

#导入整个模块 模块名.class名进行访问

import  electricCar


my_new_car = electricCar.Car('audi','a+',2018)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer = 200
my_new_car.write_odometer(800)
my_new_car.read_odometer()
my_new_car.increment_odometer(200)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()




my_elc_car = electricCar.ElectricCar("satana",'model s',2017)

electricCarInfo = my_elc_car.get_descriptive_name()


print(electricCarInfo)

my_elc_car.increment_odometer(500)
my_elc_car.read_odometer()

my_elc_car.battery.describe_barrtery()
my_elc_car.battery.get_range()
my_elc_car.fill_gas_tank()