# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


import  matplotlib.pyplot as plt


"""绘制散点图"""

#设置图标标题
plt.title("Square Numbers",fontsize = 24,color = (0.5,0.5,0.2))

#设置x轴加上标签
plt.xlabel("Value",fontsize = 14)
#设置y轴加上标签

plt.ylabel("Square of Value",fontsize = 14,color = (0.2,0.5,0.1))
#设置刻度标记的大小

plt.tick_params(axis='both',labelsize=15)

#绘制一个点
# plt.scatter(2,4)

#绘制一系列点想x,y轴传值列表

# x_values= [1,2,3,4,5]
# y_values = [1,4,9,16,25]

x_values= list(range(1,1001))
y_values = [x**2 for x in x_values]

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
#edgecolors 默认为蓝色点和黑色轮廓
# none   取消默认
# 颜色映射 （colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。
# 在可视化中，颜色映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深
# 的颜色来显示较大的值。
# 模块pyplot 内置了一组颜色映射
#cmap 置顶映射的颜色
plt.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,edgecolors='none',s = 40)

plt.show()

#自动将图标保存到文件中 替换掉plt.show()

"""
bbox_inches
第一个实参指定要以什么样的文件名保存图表；
第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空
白区域，可省略这个实参。
"""

# plt.savefig('squares_plot.png',bbox_inches = 'tight')
