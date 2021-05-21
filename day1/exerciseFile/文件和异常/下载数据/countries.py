# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'
# Pygal使用的国别码存储在模块i18n （internationalization的缩写）中。
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回pygal_maps_world使用的两个字母的国别码"""
    for code ,name in COUNTRIES.items():
        if name == country_name:
            return code

    #如果没有找到指定的国家，就返回none
    return None


# print(get_country_code('China'))
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code,COUNTRIES[country_code])







