# coding: utf-8

"""
坦克大战GUI
    新增功能
    左上角文本，显示敌方坦克剩余数量
    放置我方坦克
    增加坦克移动
"""

import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame(object):
    window = None
    myTank = None

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
        # 初始化我方坦克
        MainGame.myTank = Tank(500, 300)

        while True:
            # 监听事件
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 放置字体surface
            MainGame.window.blit(self.get_text_surface("敌方剩余坦克数量：%s" % 6), (10, 6))
            # 放置我方坦克
            MainGame.myTank.display_tank()

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    MainGame.myTank.direction = 'U'
                    MainGame.myTank.move()
                elif event.key == pygame.K_RIGHT:
                    MainGame.myTank.direction = 'R'
                    MainGame.myTank.move()
                elif event.key == pygame.K_DOWN:
                    MainGame.myTank.direction = 'D'
                    MainGame.myTank.move()
                elif event.key == pygame.K_LEFT:
                    MainGame.myTank.direction = 'L'
                    MainGame.myTank.move()


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
        self.speed = 10

    def display_tank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)

    def move(self):

        if self.direction == 'U':
            self.rect.top -= self.speed
        elif self.direction == 'R':
            self.rect.left += self.speed
        elif self.direction == 'D':
            self.rect.top += self.speed
        elif self.direction == 'L':
            self.rect.left -= self.speed





if __name__ == '__main__':
    MainGame().start_game()