# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import  requests
# from django.contrib.sites import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()

#处理结果
print(response_dict.keys())



repo_dicts = response_dict['items']
repo_dict = repo_dicts[0]
print("\nkeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print(repo_dicts)
