# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age;

    def sit(self):
        print(self.name.title() + " is now sitting")
    def roll_over(self):
        print(self.name.title() + " rolled over")



my_dog = Dog("mary",3)

print("my dog's name is " + my_dog.name.title() +".")

print("my dog's age is " +  str( my_dog.age) +" years old.")

my_dog.sit()
my_dog.roll_over()


my_dog1 = Dog("",0);
my_dog1.name = "编辑"
my_dog1.age = 6;

print("my_dog1's name is " + my_dog1.name+".")
print("my_dog1's age is " + str( my_dog.age)+" years old")



class Restaurant:
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
    def describe_restaurant(self):
        print("Restaurant's name is "+self.restaurant_name.title() + ".")
        print("Restaurant's type is " + str(self.restaurant_type) + ".")

    def open_restaurant(self):
        print("餐馆正在营业")



restaurant_ins = Restaurant("中华一条街餐馆","十里飘香")

# print(restaurant_ins.restaurant_name)
# print(restaurant_ins.restaurant_type)

restaurant_ins.describe_restaurant()

restaurant_ins.open_restaurant()



restaurant_ins1 = Restaurant("中华老字号","万里飘香")
restaurant_ins1.describe_restaurant()
restaurant_ins1.open_restaurant()




restaurant_ins2 = Restaurant("中华第一香","飘香随来")
restaurant_ins2.describe_restaurant()
restaurant_ins2.open_restaurant()




class User:

    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name

    def describe_user(self):
        print("User's name : " +str(self.first_name) + str(self.second_name)+".")

    def greet_user(self):
        print("你好, " + str(self.first_name) + self.second_name.title()+"!!!")



one_user =  User("qiao","dd")
one_user.describe_user()
one_user.greet_user()

sec_user =  User("hu","dada")
sec_user.describe_user()
sec_user.greet_user()




class Car:

    def __init__(self,make,model,year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0



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

my_new_car = Car('audi','a+',2018)
print(my_new_car.get_descriptive_name())

# my_new_car.odometer = 200
my_new_car.write_odometer(800)
my_new_car.read_odometer()
my_new_car.increment_odometer(200)
my_new_car.read_odometer()
