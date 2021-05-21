# !/usr/bin/python3
# -*- coding: UTF-8 -*-

__author__ = 'joedd'

import  random

while True:
  playe = input('(剪刀(0) 石头(1)) 布(2): \n')
  try:
        player = int(playe)

        if (player ==0 or player == 1  or player == 2) :

            com = random.randint(0,2)
            print('玩家：%d---电脑：%d'%(player,com))

            if (player == 0 and com ==2) or(player == 1 and com == 0) or (player == 2 and com==1):
                print('玩家取得了胜利')
            elif player == com :
                print('玩家平局')
            else:
                print('玩家失败')
        else:
            print('输入的无效，请输入正确的数字\n')
  except ValueError:
      print('类型错误，请输入正确的数字\n')

