#!usr/bin/env python3
# coding: utf-8

"""
飞机大战
新增功能
    新增敌方战机类
    新增子弹类
    我方战机发射子弹
"""

import pygame
from pygame.sprite import Sprite

import time

WIN_WIDTH = 480
WIN_HEIGHT = 698
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


# 基类
class BaseItem(Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


class MainGame:

    # 主窗口
    window = None
    # 玩家得分
    score = 0
    # 背景
    backGroundList = []
    # 我方战机
    myFighter = None
    # 上次按下键位
    lastKey = None
    # 我方子弹列表
    myBulletList = []

    def __init__(self):
        pass

    def start_game(self):
        # 初始化并加载主窗口
        pygame.display.init()
        # 设置主窗口大小
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption('飞机大战')
        # 创建背景
        self.create_bg()
        # 创建我方战机
        MainGame.myFighter = MyFighter(int((WIN_WIDTH - MyFighter(0, 0).rect.width)/2),
                                       int(WIN_HEIGHT*0.8))


        while True:
            time.sleep(0.02)
            # 事件处理
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 展示背景并移动
            self.blit_bg()
            # 创建并展示分数
            MainGame.window.blit(self.get_score_surface("得分: %d" % MainGame.score), (10, 6))
            # 展示我方战机, 我方战机移动, 我方战机射击
            if MainGame.myFighter:
                MainGame.myFighter.fighter_display()
                if not MainGame.myFighter.stop:
                    MainGame.myFighter.move()
                MainGame.myFighter.shot()
            # 展示我方子弹
            self.blit_my_bullet()

            # 循环更新主窗口
            pygame.display.update()

    def end_game(self):
        exit()

    def event_mgr(self):

        events = pygame.event.get()

        for event in events:
            # 窗口右上角管理按钮
            if event.type == pygame.QUIT:
                self.end_game()

            # 键盘按下
            elif event.type == pygame.KEYDOWN:
                # 记录按下的键位
                MainGame.lastKey = event.key
                if event.key == pygame.K_UP:
                    MainGame.myFighter.direction = 'U'
                    MainGame.myFighter.stop = False
                elif event.key == pygame.K_DOWN:
                    MainGame.myFighter.direction = 'D'
                    MainGame.myFighter.stop = False
                elif event.key == pygame.K_LEFT:
                    MainGame.myFighter.direction = 'L'
                    MainGame.myFighter.stop = False
                elif event.key == pygame.K_RIGHT:
                    MainGame.myFighter.direction = 'R'
                    MainGame.myFighter.stop = False

            # 键盘抬起
            elif event.type == pygame.KEYUP:
                # 防止键位影响，只有释放上次按下的键战机才会停止移动
                if event.key == MainGame.lastKey:
                    MainGame.myFighter.stop = True

    def get_score_surface(self, text):
        # 初始化字体
        pygame.font.init()
        # 创建字体
        font = pygame.font.SysFont("kaiti", 16)
        # 获取字体表面
        scoreSurface = font.render(text, True, TEXT_COLOR)
        return scoreSurface

    # 创建背景
    def create_bg(self):
        bg1 = BackGround('img/bg.gif', 0, 0)
        MainGame.backGroundList.append(bg1)
        bg2 = BackGround('img/bg.gif', 0, -WIN_HEIGHT)
        MainGame.backGroundList.append(bg2)

    # 展示背景
    def blit_bg(self):
        for bg in MainGame.backGroundList:
            bg.display_bg()
            bg.move()

    # 展示我方子弹
    def blit_my_bullet(self):

        for bullet in MainGame.myBulletList:
            # 判断子弹是否存活
            if bullet.live:
                bullet.display_bullet()
                bullet.move()
            else:
                MainGame.myBulletList.remove(bullet)


class BackGround:

    def __init__(self, filename, left, top):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 2

    def display_bg(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):

        if self.rect.top < WIN_HEIGHT:
            self.rect.top += self.speed
        else:
            self.rect.top = -WIN_HEIGHT


class Fighter(BaseItem):

    # 子弹间隔
    step = 10

    def __init__(self, left, top):
        # 形象
        self.image = pygame.image.load('img/my_fighter.gif')
        # 区域
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = 8
        # 方向
        self.direction = 'U'
        # 停止状态
        self.stop = True
        # 子弹发射间隔
        self.step = Fighter.step

    def fighter_display(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        if self.direction == 'U':
            if self.rect.top >= self.speed:
                self.rect.top -= self.speed
            else:
                self.rect.top = 0
                self.stop = True
        elif self.direction == 'D':
            if self.rect.top + self.rect.height <= WIN_HEIGHT - self.speed:
                self.rect.top += self.speed
            else:
                self.rect.top = WIN_HEIGHT - self.rect.height
                self.stop = True
        elif self.direction == 'L':
            if self.rect.left >= self.speed:
                self.rect.left -= self.speed
            else:
                self.rect.left = 0
                self.stop = True
        elif self.direction == 'R':
            if self.rect.left + self.rect.width <= WIN_WIDTH - self.speed:
                self.rect.left += self.speed
            else:
                self.rect.left = WIN_WIDTH - self.rect.width
                self.stop = True

    def shot(self):
        if self.step > 0:
            self.step -= 1
        else:
            bullet = Bullet(self)
            MainGame.myBulletList.append(bullet)
            self.step = Fighter.step


class MyFighter(Fighter):

    def __init__(self, left, top):
        super().__init__(left, top)


class EnemyFighter(Fighter):

    def __init__(self):
        super(EnemyFighter, self).__init__()

    def move(self):
        pass


class Bullet(BaseItem):

    def __init__(self, fighter):

        # 形象
        self.image = pygame.image.load('img/bullet.gif')
        # 区域
        self.rect = self.image.get_rect()
        self.rect.left = fighter.rect.left + (fighter.rect.width - self.rect.width) // 2
        self.rect.top = fighter.rect.top - self.rect.height
        # 速度
        self.speed = 10
        # 存活状态
        self.live = True

    def display_bullet(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):

        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.live = False



if __name__ == '__main__':
    MainGame().start_game()