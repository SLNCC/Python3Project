# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import json

filename = "username.json"
with open(filename) as file_obj:
    username = json.load(file_obj)
    print("Welcom back,"+username +'!!!')