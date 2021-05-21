# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


class Employee():

      def __init__(self,name,sex,salary):
            self.name = name
            self.sex = sex
            self.salary = salary
            self.allsalary = 0
            self.othersalary = 5000

      def give_raise(self,othersalary):
          if othersalary > 0:
              self.othersalary = othersalary

          self.allsalary = self.salary + self.othersalary

          return self.allsalary


