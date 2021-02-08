#!usr/bin/env python3
# coding: utf-8

import pygame
from pygame.sprite import Sprite
import random
import time

WIN_WIDTH = 600
WIN_HEIGHT = 700
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class BaseItem(Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


class MainGame:

    # 主窗口
    window = None

    def __init__(self):
        pass

    def start_game(self):
        # 初始化并加载窗口
        pygame.display.init()
        # 设置窗口尺寸
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("下一百层v1.0")

        while True:
            # 事件管理
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 展示文字内容及区域
            MainGame.window.blit(self.get_text_surface("文字内容"), (10, 6))

            # 主窗口循环
            pygame.display.update()

    def end_game(self):
        exit()

    def event_mgr(self):

        # 获取所有事件
        events = pygame.event.get()

        # 遍历所有事件
        for event in events:
            if event.type == pygame.QUIT:
                self.end_game()

    def get_text_surface(self, text):

        # 初始化字体
        pygame.font.init()
        # 设置字体格式
        font = pygame.font.SysFont("kaiti", 16)
        # 获取字体surface，参数为内容、抗锯齿、字体颜色
        textSurface = font.render(text, True, TEXT_COLOR)
        # 返回textSurface
        return textSurface


if __name__ == '__main__':
    MainGame().start_game()


