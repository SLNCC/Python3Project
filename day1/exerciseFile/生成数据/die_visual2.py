# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

from die import Die
import pygal


# 将使用Python可视化包Pygal来生成可缩放的矢量图形文件
# 创建两个D6
die_1 = Die(6)
die_2 = Die(6)

# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
#     print(results)

#列表解析：自动生成这种列表的循环
results = [ die_1.roll() + die_2.roll() for roll_num in range(1000)]

# 分析结果
# frequencies = []
max_result =  die_1.num_sides+die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

frequencies = [ results.count(value) for value in range(2,max_result +1)]

print(frequencies)



#对结果进行可视化

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"

hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist._x_title = "Result"
hist._y_title = "Frequency of request"

hist.add('D6 +D6',frequencies)

hist.render_to_file('die_visual2.svg')


