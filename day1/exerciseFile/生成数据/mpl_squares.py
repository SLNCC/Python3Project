# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]

squares = [1,4,8,16,25]

plt.plot(input_values,squares,linewidth = 5)

#设置图标标题，并给坐标轴加上标签

#设置图标标题
plt.title("Square Numbers",fontsize = 24,color = (0.5,0.5,0.2))

#设置x轴加上标签
plt.xlabel("Value",fontsize = 14)
#设置y轴加上标签

plt.ylabel("Square of Value",fontsize = 14,color = (0.2,0.5,0.1))
#设置刻度标记的大小

plt.tick_params(axis='both',labelsize=15)

plt.show()
