#!usr/bin/env python3
# coding: utf-8

"""
飞机大战
新增功能
    设置道具持续时间
"""

import pygame
from pygame.sprite import Sprite

import time
import random
import threading

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
    # 敌方战机列表：
    enemyFighterList = []
    # 爆炸效果列表
    exploreList = []
    # 道具列表
    propList = []
    # 子弹间隔
    step = 8
    # 子弹类型
    bulletType = 1

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
        self.create_my_fighter()
        # 创建背景音乐
        Music('music/bgm.wav').play(-1)

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
                MainGame.myFighter.display_fighter()
                if not MainGame.myFighter.stop:
                    MainGame.myFighter.move()
                MainGame.myFighter.shot()
                MainGame.myFighter.prop_time()
            else:
                self.create_my_fighter()
            # 展示我方子弹
            self.blit_my_bullet()
            # 创建敌方战机
            self.create_enemy_fighter()
            # 展示敌方战机
            self.blit_enemy_fighter()
            # 展示爆炸效果
            self.blit_explore()
            # 创建并展示道具
            self.create_prop()
            self.blit_prop()

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
            elif event.type == pygame.KEYDOWN and MainGame.myFighter:
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
            elif event.type == pygame.KEYUP and MainGame.myFighter:
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

    # 创建我方战机
    def create_my_fighter(self):
        MainGame.myFighter = MyFighter(int((WIN_WIDTH - MyFighter(0, 0).rect.width) / 2),
                                       int(WIN_HEIGHT * 0.8))

    # 展示我方子弹
    def blit_my_bullet(self):

        for bullet in MainGame.myBulletList:
            # 判断子弹是否存活
            if bullet.live:
                bullet.display_bullet()
                bullet.move()
                bullet.hit_fighter()
            else:
                MainGame.myBulletList.remove(bullet)

    # 创建敌方战机
    def create_enemy_fighter(self):

        num = random.randint(1, 1000)

        if num <= 10:
            enemyFighter = EnemyFighter(2)
            MainGame.enemyFighterList.append(enemyFighter)
        elif num <= 30:
            enemyFighter = EnemyFighter(1)
            MainGame.enemyFighterList.append(enemyFighter)
        elif num <= 70:
            enemyFighter = EnemyFighter(0)
            MainGame.enemyFighterList.append(enemyFighter)

    # 展示敌方战机
    def blit_enemy_fighter(self):

        for enemyFighter in MainGame.enemyFighterList:
            if enemyFighter.live:
                enemyFighter.display_fighter()
                enemyFighter.move()
                enemyFighter.hit_my_fighter()
            else:
                MainGame.enemyFighterList.remove(enemyFighter)

    # 展示爆炸效果
    def blit_explore(self):

        for explore in MainGame.exploreList:
            if explore.live:
                explore.display_explore()
            else:
                MainGame.exploreList.remove(explore)

    # 创建道具
    def create_prop(self):
        num = random.randint(0, 1199)
        if num <= 2:
            prop = Prop(num)
            MainGame.propList.append(prop)

    def blit_prop(self):

        for prop in MainGame.propList:
            if prop.live:
                prop.display_prop()
                prop.move()
                prop.hit_fighter()
            else:
                MainGame.propList.remove(prop)


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
        self.step = MainGame.step

    def display_fighter(self):
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
            if MainGame.bulletType == 1:
                bullet = Bullet(self)
                MainGame.myBulletList.append(bullet)
                # pygame.mixer.Sound('music/shot.wav').play()
            elif MainGame.bulletType == 3:
                for i in range(3):
                    bullet = Bullet(self)
                    bullet.rect.left = MainGame.myFighter.rect.left + i * (MainGame.myFighter.rect.width - 2*bullet.rect.width) // 2
                    MainGame.myBulletList.append(bullet)
            self.step = MainGame.step


class MyFighter(Fighter):

    propTimer = 300

    def __init__(self, left, top):
        super().__init__(left, top)

        self.speedStatus = False
        self.speedTimer = MyFighter.propTimer
        self.doubleStatus = False
        self.doubleTimer = MyFighter.propTimer

    def prop_time(self):
        if self.speedStatus and MainGame.myFighter:
            self.speedTimer -= 1
            if self.speedTimer <= 0:
                self.speed_end()

        if self.doubleStatus:
            self.doubleTimer -= 1
            if self.doubleTimer <= 0:
                self.double_end()

    def speed_end(self):
        self.speedStatus = False
        MainGame.step = 8

    def double_end(self):
        self.doubleStatus = False
        MainGame.bulletType = 1


class EnemyFighter(Fighter):

    def __init__(self, fighter_type, left=0, top=0):
        super(EnemyFighter, self).__init__(left, top)

        self.type = fighter_type
        self.images = [
            pygame.image.load('img/enemy_fighter0.gif'),
            pygame.image.load('img/enemy_fighter1.gif'),
            pygame.image.load('img/enemy_fighter2.gif'),
        ]
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, WIN_WIDTH-self.rect.width)
        self.rect.top = 0 - self.rect.height
        # 速度
        self.speed = random.randint(4-self.type, 7-self.type)
        # 存活状态
        self.live = True
        # 生命值
        self.hp = self.type+1
        # 分值
        self.score = 200 * (self.type+1) - 100

    def move(self):
        if self.rect.top < WIN_HEIGHT:
            self.rect.top += self.speed
        else:
            self.live = False

    def hit_my_fighter(self):

        if MainGame.myFighter and pygame.sprite.collide_rect(self, MainGame.myFighter):
            if MainGame.myFighter.speedStatus:
                MainGame.myFighter.speed_end()
            if MainGame.myFighter.doubleStatus:
                MainGame.myFighter.double_end()
            del MainGame.myFighter
            MainGame.myFighter = None


class Bullet(BaseItem):

    type = 1
    damage = 1

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

        if self.rect.top > 0 - self.rect.top:
            self.rect.top -= self.speed
        else:
            self.live = False

    def hit_fighter(self):

        for enemyFighter in MainGame.enemyFighterList:
            if pygame.sprite.collide_rect(enemyFighter, self):
                self.live = False
                enemyFighter.hp -= self.damage
                if enemyFighter.hp <= 0:
                    enemyFighter.live = False
                    explore = Explore(enemyFighter)
                    # pygame.mixer.init()
                    pygame.mixer.Sound('music/explore1.wav').play()
                    MainGame.exploreList.append(explore)
                    MainGame.score += enemyFighter.score


class Explore:

    def __init__(self, fighter):
        self.images = [
            pygame.image.load('img/explore0.gif'),
            pygame.image.load('img/explore1.gif'),
            pygame.image.load('img/explore2.gif'),
            pygame.image.load('img/explore3.gif'),
            pygame.image.load('img/explore4.gif'),
            pygame.image.load('img/explore5.gif'),
        ]

        self.image = None
        self.rect = None
        self.step = 0
        self.fighter = fighter
        self.endStep = fighter.type + 3
        self.live = True

    def display_explore(self):

        if self.step <= self.endStep:
            self.image = self.images[self.step]
            self.rect = self.image.get_rect()
            self.rect.left = self.fighter.rect.left + (self.fighter.rect.width - self.rect.width) // 2
            self.rect.top = self.fighter.rect.top + (self.fighter.rect.height - self.rect.height) // 2
            MainGame.window.blit(self.image, self.rect)
            self.step += 1
        elif self.step == self.endStep + 1:
            self.image = self.images[self.endStep-3]
            self.rect = self.image.get_rect()
            self.rect.left = self.fighter.rect.left + (self.fighter.rect.width - self.rect.width) // 2
            self.rect.top = self.fighter.rect.top + (self.fighter.rect.height - self.rect.height) // 2
            MainGame.window.blit(self.image, self.rect)
            self.step += 1
        else:
            self.live = False
            self.step = self.endStep


class Music:

    def __init__(self, filename):
        self.filename = filename
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)

    def play(self, loops=0, start=0.0):
        pygame.mixer.music.play(loops=loops, start=start)
        pygame.mixer.music.set_volume(0.2)


class Prop(BaseItem):

    def __init__(self, prop_type):
        self.images = [
            pygame.image.load('img/speed.gif'),
            pygame.image.load('img/boom.gif'),
            pygame.image.load('img/double.gif'),
        ]
        self.type = prop_type
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, WIN_WIDTH-self.rect.width)
        self.rect.top = -self.rect.height
        self.speed = 4
        self.live = True

    def display_prop(self):
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        if self.rect.top < WIN_HEIGHT:
            self.rect.top += self.speed
        else:
            self.live = False

    def hit_fighter(self):
        if MainGame.myFighter and pygame.sprite.collide_rect(self, MainGame.myFighter):
            if self.type == 0:
                MainGame.step = 1
                self.live = False
                MainGame.myFighter.speedStatus = True
                MainGame.myFighter.speedTimer = MyFighter.propTimer
            elif self.type == 1:
                for enemyFighter in MainGame.enemyFighterList:
                    self.live = False
                    enemyFighter.live = False
                    explore = Explore(enemyFighter)
                    MainGame.exploreList.append(explore)
                    MainGame.score += enemyFighter.score
                pygame.mixer.Sound('music/explore1.wav').play()
            elif self.type == 2:
                self.live = False
                MainGame.myFighter.doubleStatus = True
                MainGame.myFighter.doubleTimer = MyFighter.propTimer
                MainGame.bulletType = 3


if __name__ == '__main__':
    MainGame().start_game()