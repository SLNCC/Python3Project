# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import json


filename = 'number.json'
with open(filename) as file_obj:
    numbers = json.load(file_obj)


print(numbers)
