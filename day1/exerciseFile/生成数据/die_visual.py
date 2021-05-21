# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

from die import Die
import pygal


# 将使用Python可视化包Pygal来生成可缩放的矢量图形文件
# 创建一个D6
die = Die(6)
# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#     print(results)

results = [die.roll() for roll_num in range(1000) ]
# 分析结果
# frequencies = []
# for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)



frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
print(frequencies)


#对结果进行可视化

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"

hist.x_labels = ['1','2','3','4','5','6']
hist._x_title = "Result"
hist._y_title = "Frequency of request"

hist.add('D6',frequencies)

hist.render_to_file('die_visual.svg')


