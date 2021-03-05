#!usr/bin/env python3
# coding: utf-8

import pygame
from pygame.sprite import Sprite
import random
import time

WIN_WIDTH = 600
WIN_HEIGHT = 800
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class BaseItem(Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


class MainGame:

    # 主窗口
    window = None
    # 侧边墙壁列表
    sideWallList = []
    # 当前层数
    floor = 0
    # 墙体速度
    wallSpeed = 2
    # 墙壁列表
    wallList = []
    # 墙壁步长
    wallStep = 0
    # 总高度
    sumSpeed = 0
    # 主角
    man = None
    # 记录上一次按下的键位
    lastKey = None

    def __init__(self):
        pass

    def start_game(self):
        # 初始化并加载窗口
        pygame.display.init()
        # 设置窗口尺寸
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("下一百层v1.0")
        # 创建顶部墙壁
        topWall = TopWall()
        # 创建侧边墙壁
        self.create_side_wall()
        # 创建初始墙壁
        self.create_initial_wall()
        # 创建主角
        MainGame.man = Man(MainGame.wallList[0])


        while True:
            # 降低刷新频率
            time.sleep(0.02)
            # 事件管理
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 展示侧边墙壁
            self.blit_side_wall()
            # 展示顶部墙壁
            topWall.display_top_wall()
            # 展示文字内容及区域
            MainGame.sumSpeed += MainGame.wallSpeed
            MainGame.window.blit(self.get_text_surface("当前层数：B%05d" % (MainGame.sumSpeed // 500)), (25, 30))
            # 游戏过程中创建墙壁
            self.create_wall()
            # 展示墙壁
            self.blit_wall()
            if MainGame.man and MainGame.man.live:
                # 展示主角
                MainGame.man.display_man()
                # 主角移动
                if not MainGame.man.stop:
                    MainGame.man.horizontal_move()
                if not MainGame.man.verticalStop:
                    MainGame.man.vertical_move()
            else:
                self.man_reborn()

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

            if event.type == pygame.KEYDOWN:
                MainGame.lastKey = event.key
                if event.key == pygame.K_LEFT:
                    MainGame.man.direction = "L"
                    MainGame.man.stop = False
                elif event.key == pygame.K_RIGHT:
                    MainGame.man.direction = "R"
                    MainGame.man.stop = False

            if event.type == pygame.KEYUP:
                if event.key == MainGame.lastKey:
                    MainGame.man.stop = True

    def get_text_surface(self, text):

        # 初始化字体
        pygame.font.init()
        # 设置字体格式
        font = pygame.font.SysFont("kaiti", 16)
        # 获取字体surface，参数为内容、抗锯齿、字体颜色
        textSurface = font.render(text, True, TEXT_COLOR)
        # 返回textSurface
        return textSurface

    # 创建侧面墙壁
    def create_side_wall(self):
        for i in range(2):
            sideWall = SideWall(0, i*WIN_HEIGHT+abs(i-1)*50)
            MainGame.sideWallList.append(sideWall)

    # 展示侧面墙壁
    def blit_side_wall(self):
        for sideWall in MainGame.sideWallList:
            sideWall.display_side_wall()
            sideWall.move()

    # 创建初始墙壁
    def create_initial_wall(self):

        for i in range(1, 6):
            num = random.randint(80, 100)
            wall = Wall("normal", num+i*160)
            MainGame.wallList.append(wall)

    # 游戏过程中创建墙壁
    def create_wall(self):
        if MainGame.wallStep > 0:
            MainGame.wallStep -= 1
        else:
            num = random.randint(80, 100) + 180
            wall = Wall('normal', WIN_HEIGHT+num)
            MainGame.wallList.append(wall)
            MainGame.wallStep = num // MainGame.wallSpeed / 2

    # 展示墙壁
    def blit_wall(self):

        for wall in MainGame.wallList:
            if wall.live:
                wall.display_wall()
                wall.move()
                # 判断是否与人接触
                wall.man_stand()
            else:
                MainGame.wallList.remove(wall)

    # 主角重生
    def man_reborn(self):

        for wall in MainGame.wallList:
            if 250 <= wall.rect.top <= 550:
                MainGame.man = Man(wall)
                break


class TopWall(BaseItem):

    def __init__(self):

        self.image1 = pygame.image.load('img/topbg.gif')
        self.image2 = pygame.image.load('img/top2.gif')

    def display_top_wall(self):

        MainGame.window.blit(self.image2, (25, 50))
        MainGame.window.blit(self.image1, (0, 0))


class SideWall:

    def __init__(self, left, top):

        self.image = pygame.image.load('img/side.gif')

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        # self.speed = 4

    def display_side_wall(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        if self.rect.top + self.rect.height > 60:
            self.rect.top -= MainGame.wallSpeed
        else:
            self.rect.top = WIN_HEIGHT


class Man(Sprite):

    def __init__(self, wall):
        self.images = [
            pygame.image.load('img/ss0.gif'),
            pygame.image.load('img/ss1.gif'),
            pygame.image.load('img/ss2.gif'),
        ]
        self.step = 0
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.left = wall.rect.left + (wall.rect.width - self.rect.width)//2
        self.rect.top = wall.rect.top - self.rect.height
        self.horizontalSpeed = 8
        self.verticalSpeed = 0
        self.direction = 'L'
        self.stop = True
        self.verticalStop = False
        self.live = True
        self.acceleration = 2
        self.timer = 1

    def display_man(self):
        if self.stop:
            MainGame.window.blit(self.image, self.rect)
        else:
            if self.step <= 29:
                MainGame.window.blit(self.images[self.step//10], self.rect)
                self.step += 1
            else:
                self.step = 0

    def horizontal_move(self):
        if self.direction == 'L':
            if self.rect.left > 25 + self.horizontalSpeed:
                self.rect.left -= self.horizontalSpeed
            else:
                self.rect.left = 25
                self.stop = True
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WIN_WIDTH - 25 - self.horizontalSpeed:
                self.rect.left += self.horizontalSpeed
            else:
                self.rect.left = WIN_WIDTH - 25 - self.rect.width
                self.stop = True

    def vertical_move(self):

        if self.timer >= 0:
            self.timer -= 1
        else:
            self.verticalSpeed += self.acceleration
            self.timer = 2

        if self.rect.top + self.rect.height <= WIN_HEIGHT:
            self.rect.top += self.verticalSpeed
        else:
            self.live = False


class Wall(Sprite):

    def __init__(self, wall_type, top):

        self.type = wall_type
        self.images = {
            "normal": [
                pygame.image.load('img/normal_wall0.gif'),
                pygame.image.load('img/normal_wall1.gif'),
                pygame.image.load('img/normal_wall2.gif'),
            ]

        }
        self.image = self.images[wall_type][random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(25, WIN_WIDTH-25-self.rect.width)
        self.rect.top = top
        # self.speed=
        self.live = True

    def display_wall(self):

        MainGame.window.blit(self.image, self.rect)

    def move(self):
        if self.rect.top >= 50:
            self.rect.top -= MainGame.wallSpeed
        else:
            self.live = False

    def man_stand(self):

        if MainGame.man and MainGame.man.live:
            if pygame.sprite.collide_rect(self, MainGame.man):
                if MainGame.man.verticalSpeed:
                    MainGame.man.verticalStop = True
                    MainGame.man.verticalSpeed = 0
                MainGame.man.rect.top = self.rect.top - MainGame.man.rect.height
            else:
                MainGame.man.verticalStop = False



if __name__ == '__main__':
    MainGame().start_game()


