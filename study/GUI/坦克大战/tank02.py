# coding: utf-8

"""
坦克大战GUI
    新增功能
    添加事件管理：
    1. 退出
    2. 坦克移动

"""

import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
BG_COLOR = (0, 0, 0)


class MainGame(object):
    window = None

    def __init__(self):
        pass

    # 开始游戏
    def start_game(self):
        # 加载并初始化主窗口
        pygame.display.init()
        # 设置窗口大小
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])

        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.0")

        while True:
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 监听事件
            self.event_mgr()

            # 主窗口循环
            pygame.display.update()

    # 结束游戏
    def end_game(self):
        print("游戏结束")
        exit()

    # 事件管理
    def event_mgr(self):

        events = pygame.event.get()

        for event in events:
            # 退出
            if event.type == pygame.QUIT:
                self.end_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("上")
                elif event.key == pygame.K_RIGHT:
                    print("右")
                elif event.key == pygame.K_DOWN:
                    print("下")
                elif event.key == pygame.K_LEFT:
                    print("左")





if __name__ == '__main__':
    MainGame().start_game()