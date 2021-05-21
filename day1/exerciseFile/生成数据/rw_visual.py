# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'
import  matplotlib.pyplot as plt
from  random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    # dpi:屏幕分辨率    为80像素/英寸
    plt.figure(dpi= 128,figsize=(10, 6))

    num_points = list(range(rw.num_points))
    #
    # plt.scatter(rw.x_values, rw.y_values, c=num_points,cmap=plt.cm.Blues,edgecolors='none',s=15)
    #
    # # 突出起点和终点
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    #             s=100)


    plt.plot(rw.x_values, rw.y_values,linewidth = 1.0)




    #隐藏坐标轴

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk / (y/n)")
    if keep_running == 'n':
        break


