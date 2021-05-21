# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

from die import Die
import pygal




def rangeResults(max_range):
    # max_range = 1000
    #
    # 将使用Python可视化包Pygal来生成可缩放的矢量图形文件
    # 创建一个D8
    die_1 = Die(8)

    die_2 = Die(8)

    # 掷几次骰子，并将结果存储在一个列表中

    # 列表解析：自动生成这种列表的循环
    results = [die_1.roll() + die_2.roll() for roll_num in range(max_range)]

    # 分析结果
    # frequencies = []
    max_result = die_1.num_sides + die_2.num_sides

    frequencies = [results.count(value) for value in range(2, max_result + 1)]

    print(frequencies)

    # 对结果进行可视化

    hist = pygal.Bar()

    hist.title = "Results of rolling one D8 1000 times"

    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    hist._x_title = "Result"
    hist._y_title = "Frequency of request"

    hist.add('D8', frequencies)

    hist.render_to_file('die_visual4.svg')




rangeResults(1000)


while True:
    x = int(input('Enter a number for x: '))
    max_range = x +1000

    rangeResults(max_range)

