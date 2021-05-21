# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import pygame
import os
class GameStats():

    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = True

        #在任何情况下都不应该重置最高分数
        self.high_score = 0
        self.get_high_score()


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        #飞船的个数
        self.ships_left = self.ai_settings.ship_limit

        self.score = 0
        #当前等级---确保开始新游戏重置等级
        self.level = 1

    def  get_high_score(self):
        
        if os.path.exists('high_score.text'):
            with open('high_score.text','r') as  file_obj:
                readline = file_obj.readline()
                print(readline)
                if readline:
                    self.high_score = int(readline)
        else:
            with  open('high_score.text','w') as file_obj:
                if file_obj :
                    print("创建成功")


