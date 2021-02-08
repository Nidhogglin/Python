# coding: utf-8

"""
坦克大战GUI
1. 加载主窗口
"""

import pygame

WIN_WIDTH = 700
WIN_HEIGHT = 500
BG_COLOR = (0, 0, 0)


class MainGame(object):
    window = None

    def __init__(self):
        pass

    def start_game(self):
        # 加载并初始化主窗口
        pygame.display.init()
        # 设置窗口大小
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])

        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.0")

        while True:
            MainGame.window.fill(BG_COLOR)
            pygame.display.update()



if __name__ == '__main__':
    MainGame().start_game()