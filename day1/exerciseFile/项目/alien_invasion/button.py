# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import  pygame

class Button():

    def __init__(self,ai_settings,screen,msg):

        """初始化按钮"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他的属性

        self.width ,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #创建按钮的rect对象，并是其居中

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        #按钮的标签只需要创建一次--Pygame通过将你要显示的字符串渲染为图像来处理文本。

        self.prep_msg(msg) #调用prep_msg() 来处理这样的渲染。

    def prep_msg(self,msg):

        """将msg渲染为图像，并使其在按钮上居中"""
        """
          1.调用font.render() 将存储在msg 中的文本转换为图像 布尔值：反锯齿让文本的边缘更平滑
          2.存储在msg_image 中
        
        """
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)  #绘制表示按钮的矩形

        # 并向screen.blit()传递一幅图像以及与该图像相关联的rect
        # 对象，从而在屏幕上绘制文本图像。
        self.screen.blit(self.msg_image, self.msg_image_rect)


