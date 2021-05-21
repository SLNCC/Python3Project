# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'


class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #设置飞船
        self.ship_limit = 2
        self.ship_width = 60
        self.ship_height = 60




        # 设置子弹的属性
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3




        #给外星人添加属性
        self.fleet_drop_speed = 10  #指定了有外星人撞到屏幕边缘时，外星人群向下移动的速度


        #以什么样的速度加快游戏的节凑
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""


        self.ship_speed_factor = 3.0    #飞船的速度

        self.bullet_speed_factor = 3    #子弹的速度  这项设置的最佳值取决于你的系统速度

        self.alien_speed_factor = 10    #外星人的速度

        #fleet_direction 为1表示向右移，为-1表示向左移动
        self.fleet_direction = 1
        #外星人点数的提高的速度
        self.score_scale = 1.5


        # 记分
        self.alien_points = 50



    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # 记分
        self.alien_points = int(self.alien_points * self.score_scale)

        print(self.alien_points)

