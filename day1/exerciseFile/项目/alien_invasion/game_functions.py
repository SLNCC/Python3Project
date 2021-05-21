# !/usr/bin/python3
# -*- coding: UTF-8 -*-
from time import sleep

__author__ = 'joedd'
import sys
import pygame

from  bullet import  Bullet
from  alien import Alien


def check_keydown_events(event,stats,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:#275
        ship.moving_right = True

    elif event.key == pygame.K_LEFT: #276
        ship.moving_left = True

    elif event.key == pygame.K_UP:#273
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:#274
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        with  open('high_score.text', 'w') as file_obj:
            file_obj.write(str(stats.high_score))
        sys.exit()




    # print(event.key)
    #上右下左

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组bullets中

    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ai_settings,screen,ship,bullets):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False



def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():  # 循环监听事件
        if event.type == pygame.QUIT:  # ，点击关闭按钮时，将检测到pygame.QUIT 事件
            sys.exit()  # 退出游戏
        elif event.type == pygame.KEYDOWN:
            #向右移动飞船
            check_keydown_events(event,stats,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.MOUSEBUTTONDOWN:#鼠标点击事件
            #获取当前鼠标的位置x,y
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #判断事件是否在按钮范围内
            check_play_button(ai_settings,screen,stats ,sb,play_button,ship,aliens,bullets, mouse_x, mouse_y)


def check_play_button(ai_settings,screen, stats,sb, play_button,ship,aliens,bullets,mouse_x, mouse_y):
    """在玩家点击Play按钮时开始新游戏"""
    button_clicked =  play_button.rect.collidepoint(mouse_x,mouse_y)

    #而这个函数使用collidepoint() 检查鼠标单击位置是否在Play按钮的rect 内
    if button_clicked and not stats.game_active:
        #玩家结束，重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)

        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #重置积分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()


        #创建一群外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.ret_center_ship()







def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""

    # 每次循环时，都会重绘屏幕
    screen.fill(ai_settings.bg_color)  # 接受实参

    #在飞船和外星人后面重绘所有子弹

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 显示记分
    sb.show_score()

    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除消失的子弹"""

    #更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        # 在for 循环中，不应从列表或编组中删除条目，
        # 因此必须遍历编组的副本。我们使用了方法copy() 来设置for 循环
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)




def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人
    # 如果是这样，就删除相应的子弹和外星人
    """
       新增的这行代码遍历编组bullets 中的每颗子弹，再遍历编组aliens 中的每个外星人。
       每当有子弹和外星人的rect 重叠时，groupcollide() 就在它返回的字典中添加一
       个键-值对。两个实参True 告诉Pygame删除发生碰撞的子弹和外星人。
        （要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，可将第一个布尔实参设置
        为False ，并让第二个布尔实参为True 。这样被击中的外星人将消失，但所有的子弹都始终有效，
        直到抵达屏幕顶端后消失。）
    """
    # 检测子弹和外星人的碰撞
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # print(len(bullets))
    if collisions:
        # stats.score += ai_settings.alien_points
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points *len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    # 生成新的外星人
    if len(aliens) == 0:
        # 删除所有的子弹,加快游戏节凑,创建一群外星人
        #如果整群外星人都被消灭，就提高一个等级
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats,sb):

    """检查是否诞生最高得分"""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



def get_number_aliens_x(ai_settings,alien_width):
    """每一行可以容乃多少行外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人将其放到当前位置"""
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x

    alien.rect.y = alien.rect.height + 2 * alien.rect.height  * row_number

    aliens.add(alien)




def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)

    alien_width = alien.rect.width

    number_aliens_x = get_number_aliens_x(ai_settings,alien_width)

    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                alien.rect.height)
    #创建外星人群
    for row_number in range(number_rows):
        print(str( row_number))

        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number,row_number)



def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):

    """响应被外星人撞到飞船"""
    #将ships_left 减1

    if stats.ships_left > 0:
        stats.ships_left -= 1
        #更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)



def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检测是否有外星人到达了屏幕低端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >=  screen_rect.bottom:
            #像飞船撞到一样进行处理
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break





def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):

    """检测是否有外星人人到达屏幕边缘，然后更新外星人所有的位置"""

    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit !!!")
        # ai_settings.fleet_drop_speed = 50
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    # 检测是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)























