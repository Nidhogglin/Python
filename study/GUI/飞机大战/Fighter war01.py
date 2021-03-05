#!usr/bin/env python3
# coding: utf-8

"""
飞机大战
"""

import pygame
from pygame.sprite import Sprite

import time

WIN_WIDTH = 500
WIN_HEIGHT = 600
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
    # 我方战机
    myFighter = None

    def __init__(self):
        pass

    def start_game(self):
        # 初始化并加载主窗口
        pygame.display.init()
        # 设置主窗口大小
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption('飞机大战')
        # 创建我方战机
        MainGame.myFighter = MyFighter(int((WIN_WIDTH - MyFighter(0, 0).rect.width)/2),
                                       int(WIN_HEIGHT*0.8))

        while True:
            time.sleep(0.02)
            # 事件处理
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 创建并展示分数
            MainGame.window.blit(self.get_score_surface("得分: %d" % MainGame.score), (10, 6))
            # 展示我方战机
            MainGame.myFighter.fighter_display()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('上')
                elif event.key == pygame.K_DOWN:
                    print('下')
                elif event.key == pygame.K_LEFT:
                    print('左')
                elif event.key == pygame.K_RIGHT:
                    print('右')

    def get_score_surface(self, text):
        # 初始化字体
        pygame.font.init()
        # 创建字体
        font = pygame.font.SysFont("kaiti", 16)
        # 获取字体表面
        scoreSurface = font.render(text, True, TEXT_COLOR)
        return scoreSurface


class Fighter(BaseItem):

    def __init__(self, left, top):
        # 形象
        self.image = pygame.image.load('img/my_fighter.gif')
        # 区域
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = 8

    def fighter_display(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        pass


class MyFighter(Fighter):

    def __init__(self, left, top):
        super().__init__(left, top)





if __name__ == '__main__':
    MainGame().start_game()