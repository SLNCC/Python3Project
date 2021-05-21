# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import pygame

from  settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats

from  scoreboard import Scoreboard


from button import Button

from pygame.sprite import Group
import  game_functions as gf



def run_game():
    #初始化游戏,设置和屏幕对象

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)) #这个游戏的所有图形元素都将在其中绘制 (1200,800) 元组
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    stats.get_high_score()

    #创建记分牌
    sb = Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)



    #创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建一个外星人
    gf.create_fleet(ai_settings, screen,ship,aliens)
    # alien = Alien(ai_settings, screen)


    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)



        if stats.game_active:
            # 移动位置
            ship.update()
            # 子弹的绘制
            gf.update_bullets(ai_settings, screen,stats,sb ,ship, aliens, bullets)
            # 外星人移动起来
            gf.update_aliens(ai_settings, stats,sb,screen, ship, aliens, bullets)


        #飞船的屏幕显示的位置
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)



        pygame.display.flip()


run_game()





















"""
1.对象screen 是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。display.set_mode()
返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。
"""