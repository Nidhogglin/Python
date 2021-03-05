# coding: utf-8

"""
坦克大战GUI
    新增功能
    优化坦克移动
"""

import pygame
import time

WIN_WIDTH = 1000
WIN_HEIGHT = 600
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame(object):
    window = None
    myTank = None

    def __init__(self):
        # 记录上一次按的键
        self.keyLast = None

    # 开始游戏
    def start_game(self):
        # 加载并初始化主窗口
        pygame.display.init()
        # 设置窗口大小
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.0")
        # 初始化我方坦克
        MainGame.myTank = Tank(500, 300)

        while True:
            time.sleep(0.02)
            # 监听事件
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 放置字体surface
            MainGame.window.blit(self.get_text_surface("敌方剩余坦克数量：%s" % 6), (10, 6))
            # 放置我方坦克
            MainGame.myTank.display_tank()
            # 坦克移动
            if not MainGame.myTank.stop:
                MainGame.myTank.move()

            # 主窗口循环
            pygame.display.update()

    # 结束游戏
    def end_game(self):
        print("游戏结束")
        exit()

    def get_text_surface(self, text):

        # 初始化字体
        pygame.font.init()
        # 设置自动样式
        font = pygame.font.SysFont("kaiti", 18)
        # 获取字体surface
        textSurface = font.render(text, True, TEXT_COLOR)
        # 返回字体surface
        return textSurface

    # 事件管理
    def event_mgr(self):

        events = pygame.event.get()

        for event in events:
            # 退出
            if event.type == pygame.QUIT:
                self.end_game()

            # 键位按下
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    MainGame.myTank.direction = 'U'
                    MainGame.myTank.stop = False
                    self.keyLast = pygame.K_UP
                elif event.key == pygame.K_RIGHT:
                    MainGame.myTank.direction = 'R'
                    MainGame.myTank.stop = False
                    self.keyLast = pygame.K_RIGHT
                elif event.key == pygame.K_DOWN:
                    MainGame.myTank.direction = 'D'
                    MainGame.myTank.stop = False
                    self.keyLast = pygame.K_DOWN
                elif event.key == pygame.K_LEFT:
                    MainGame.myTank.direction = 'L'
                    MainGame.myTank.stop = False
                    self.keyLast = pygame.K_LEFT
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")

            # 键位抬起
            if event.type == pygame.KEYUP:
                # 如果是方向键抬起，停止坦克移动
                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or \
                #         event.key == pygame.K_RIGHT:
                #     MainGame.myTank.stop = True
                if event.key == self.keyLast:
                    MainGame.myTank.stop = True




class Tank(object):

    def __init__(self, left, top):

        # load()返回surface对象
        self.images = {
            "U": pygame.image.load("img/my_tankU.gif"),
            "R": pygame.image.load("img/my_tankR.gif"),
            "D": pygame.image.load("img/my_tankD.gif"),
            "L": pygame.image.load("img/my_tankL.gif")
        }

        # 设置初始方向
        self.direction = 'U'
        # 根据方向获取图片
        self.image = self.images[self.direction]
        # 获取图片区域
        self.rect = self.image.get_rect()
        # 设置区域初始位置
        self.rect.left = left
        self.rect.top = top
        # 设置初始速度
        self.speed = 5
        # 设置开关状态
        self.stop = True

    def display_tank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)

    def move(self):

        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WIN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WIN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed





if __name__ == '__main__':
    MainGame().start_game()