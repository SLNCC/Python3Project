# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import  unittest

from  employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('qiaodd','m',2000)
        self.allsalary = 0

    def test_give_default_raise(self):
        print('-----------')
        self.allsalary = self.employee.give_raise(0)
        print("默认年薪增加量的总额： " + str(self.allsalary))
    def test_give_custom_raise(self):
        print('-----------')
        self.allsalary =  self.employee.give_raise(8000)
        print("其他的年薪增加量的总额： " + str(self.allsalary))