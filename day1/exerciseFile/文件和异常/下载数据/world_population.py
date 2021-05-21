# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from typing import Dict, Any

__author__ = 'joedd'

import json
from countries import get_country_code
import pygal_maps_world.maps
import pygal
from pygal.style import RotateStyle as RS , LightColorizedStyle as LCS

# Python不能直接将包含小数点的字符串'1127437398.85751' 转换为整数
#正确操作：先转成float 再转化成整数

filename = 'population_data.json'


with open(filename) as obj:
    pop_data = json.load(obj)

#
# for pop_dic in pop_data:
#     if pop_dic['Year'] == '2010':
#         country_name = pop_dic['Country Name']
#         country_population = int(float(pop_dic['Value']))
#         code = get_country_code(country_name)
#         # print(country_name +": " + str(country_population))
#
#
#         if code:
#             print(code + ": "+str(country_population))
#         else:
#             print('ERROR-'+ country_name)



#创建一个包含人口的数据的字典
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year']  == '2010':
        country = pop_dict['Country Name']
        population = int (float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

        print(cc_populations)


#根据人口数量将所有的国家分成三组

# cc_pops_3: Dict[Any, int]
# cc_pops_2: Dict[Any, int]
#
# cc_pops_1: Dict[Any, int]

cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}


for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))


wm_style = RS('#336699',base_style=LCS)
wm =  pygal_maps_world.maps.World(style = wm_style)

# wm = pygal.maps.world.world()
wm.title = 'World Population in 2010 by Country'
# wm.add('2010',cc_populations)

wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')
