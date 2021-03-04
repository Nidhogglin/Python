#!usr/bin/env python3
# coding: utf-8

import pygame
from pygame.sprite import Sprite
import random
import time
import math

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
    # 顶部墙壁
    topWall = None
    # 侧边墙壁列表
    sideWallList = []
    # 当前层数
    floor = 0
    # 墙体速度
    wallSpeed = 3
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
    # 游戏开始暂停状态
    flag = False

    def __init__(self):
        pass

    def start_game(self):
        # 初始化并加载窗口
        pygame.display.init()
        # 设置窗口尺寸
        MainGame.window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("下一百层v1.0")
        # 初始化混音器
        pygame.mixer.init()
        # 播放背景音乐
        pygame.mixer.music.load('music/BGM.mp3')
        pygame.mixer.music.play(-1, 5)
        pygame.mixer.music.set_volume(0.2)
        # 创建顶部墙壁
        MainGame.topWall = TopWall()
        # 创建侧边墙壁
        self.create_side_wall()
        # 创建初始墙壁
        self.create_initial_wall()
        # 创建主角
        MainGame.man = Man(MainGame.wallList[0])
        # 创建顶部背景
        topBG = pygame.image.load('img/topbg.gif')
        # 最高记录
        maxFloor = 0

        while True:
            while MainGame.flag:
                # 降低刷新频率
                time.sleep(0.02)
                # 事件管理
                self.event_mgr()
                # 填充背景色
                MainGame.window.fill(BG_COLOR)
                # 展示侧边墙壁
                self.blit_side_wall()
                # 展示顶部墙壁
                MainGame.window.blit(topBG, (0, 0))
                MainGame.topWall.display_top_wall()
                # 展示文字内容及区域
                MainGame.sumSpeed += MainGame.wallSpeed
                floor = MainGame.sumSpeed // 300
                MainGame.wallSpeed = 3 + math.sqrt(floor) // 2.7
                MainGame.window.blit(self.get_text_surface("当前层数：B%05d" % floor), (25, 30))
                # 展示最高层数
                maxFloor = max(maxFloor, floor)
                MainGame.window.blit(self.get_text_surface("最高层数：B%05d" % maxFloor), (200, 30))
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
                    # 是否撞到顶部墙壁
                    MainGame.man.hit_top_wall()
                else:
                    MainGame.sumSpeed = 0
                    self.man_reborn()

                # 主窗口循环
                pygame.display.update()

            while not MainGame.flag:
                # 降低刷新频率
                time.sleep(0.02)
                # 事件管理
                self.event_mgr()
                # 填充背景色
                MainGame.window.fill(BG_COLOR)
                # 展示侧边墙壁
                self.blit_side_wall()
                # 展示顶部墙壁
                MainGame.window.blit(topBG, (0, 0))
                MainGame.topWall.display_top_wall()
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
                if event.key == pygame.K_SPACE:
                    if MainGame.flag:
                        MainGame.flag = False
                    else:
                        MainGame.flag = True
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
            wall = Wall(num+i*160)
            MainGame.wallList.append(wall)

    # 游戏过程中创建墙壁
    def create_wall(self):
        if MainGame.wallStep > 0:
            MainGame.wallStep -= 1
        else:
            num = random.randint(80, 100) + 180
            num2 = random.randint(1, 8)
            if num2 == 1:
                wall = HurtWall(WIN_HEIGHT+num)
            elif num2 == 2:
                wall = MoveWall(WIN_HEIGHT+num)
            else:
                wall = Wall(WIN_HEIGHT+num)
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
            if wall.type != 'hurt' and 250 <= wall.rect.top <= 550:
                MainGame.man = Man(wall)
                break


class TopWall(BaseItem):

    def __init__(self):

        self.image2 = pygame.image.load('img/top2.gif')
        self.rect = self.image2.get_rect()
        self.rect.left = 25
        self.rect.top = 50

    def display_top_wall(self):

        MainGame.window.blit(self.image2, self.rect)


class SideWall:

    def __init__(self, left, top):

        self.image = pygame.image.load('img/side.gif')

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

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
        # 形象
        self.step = 0
        self.image = self.images[1]
        # 区域
        self.rect = self.image.get_rect()
        self.rect.left = wall.rect.left + (wall.rect.width - self.rect.width)//2
        self.rect.top = wall.rect.top - self.rect.height
        # 水平速度
        self.horizontalSpeed = 10
        # 垂直速度
        self.verticalSpeed = 0
        # 方向
        self.direction = 'L'
        # 水平运动状态
        self.stop = True
        # 垂直运动状态
        self.verticalStop = True
        # 存活状态
        self.live = True
        # 加速度
        self.acceleration = 2
        # 加速频率
        self.timer = 1
        # 死亡音乐
        self.music = pygame.mixer.Sound('music/stand.wav')
        self.music.set_volume(0.6)

    def display_man(self):
        if self.stop:
            MainGame.window.blit(self.image, self.rect)
        else:
            if self.step <= 14:
                MainGame.window.blit(self.images[self.step//5], self.rect)
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
            self.timer = 1

        if self.rect.top + self.rect.height <= WIN_HEIGHT:
            self.rect.top += self.verticalSpeed
        else:
            self.live = False
            self.die_music()

    def hit_top_wall(self):

        if MainGame.man.live and pygame.sprite.collide_rect(self, MainGame.topWall):
            self.live = False
            self.die_music()

    def die_music(self):
        self.music.play()

class Wall(Sprite):

    def __init__(self, top):

        self.type = 'normal'
        self.images = {
            "normal": [
                pygame.image.load('img/normal_wall0.gif'),
                pygame.image.load('img/normal_wall1.gif'),
                pygame.image.load('img/normal_wall2.gif'),
            ]

        }
        self.image = self.images['normal'][random.randint(0, 2)]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(25, WIN_WIDTH-25-self.rect.width)
        self.rect.top = top
        self.live = True
        self.flag = False

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
                self.flag = True
                if not MainGame.man.verticalStop:
                    MainGame.man.verticalStop = True
                    MainGame.man.verticalSpeed = 0
                MainGame.man.rect.top = self.rect.top - MainGame.man.rect.height
            else:
                if self.flag:
                    MainGame.man.verticalStop = False
                    self.flag = False


class HurtWall(Wall):

    def __init__(self, top):
        super().__init__(top)
        self.type = 'hurt'

        self.image = pygame.image.load('img/hurt_wall.gif')
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(25, WIN_WIDTH-25-self.rect.width)
        self.rect.top = top

    def man_stand(self):
        if MainGame.man and MainGame.man.live:
            if pygame.sprite.collide_rect(self, MainGame.man):
                MainGame.man.live = False
                MainGame.man.die_music()


class MoveWall(Wall):

    def __init__(self, top):
        super().__init__(top)

        self.typeInt = random.randint(0, 1)
        if self.typeInt:
            self.type = 'L'
        else:
            self.type = 'R'
        self.images = {
            "L": [
                pygame.image.load('img/left_wall1.gif'),
                pygame.image.load('img/left_wall2.gif')
            ],
            "R": [
                pygame.image.load('img/right_wall1.gif'),
                pygame.image.load('img/right_wall2.gif')
            ]
        }
        self.image = self.images[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(25, WIN_WIDTH - 25 - self.rect.width)
        self.rect.top = top
        self.step = 11
        self.status = 1
        self.flag = False

    def display_wall(self):
        if self.step >= 0:
            self.step -= 1
        else:
            self.step = 11
        MainGame.window.blit(self.images[self.type][self.step // 6], self.rect)

    def man_stand(self):
        if MainGame.man and MainGame.man.live:
            if pygame.sprite.collide_rect(self, MainGame.man):
                self.flag = True
                if MainGame.man.verticalSpeed:
                    MainGame.man.verticalStop = True
                    MainGame.man.verticalSpeed = 0
                if self.type == 'L':
                    MainGame.man.rect.left -= 5
                else:
                    MainGame.man.rect.left += 5
                MainGame.man.rect.top = self.rect.top - MainGame.man.rect.height
            else:
                if self.flag:
                    MainGame.man.verticalStop = False
                    self.flag = False


if __name__ == '__main__':
    MainGame().start_game()


