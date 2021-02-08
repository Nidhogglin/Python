# coding: utf-8

"""
坦克大战GUI
    新增功能
    限制子弹数量
    子弹碰壁消失
"""

import pygame
import time
import random

WIN_WIDTH = 1000
WIN_HEIGHT = 600
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame(object):
    window = None
    myTank = None
    # 创建敌方坦克列表
    enemyTankList = []
    # 设置敌方坦克数量
    enemyTankCount = 6
    # 创建我方子弹列表
    myBulletList = []
    # 限制子弹数量
    myBulletCount = 5

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
        MainGame.myTank = MyTank(WIN_WIDTH*0.5-25, WIN_HEIGHT*0.9-25)
        # 初始化敌方坦克
        self.create_enemy_tank()

        while True:
            time.sleep(0.02)
            # 监听事件
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 放置字体surface
            MainGame.window.blit(self.get_text_surface("敌方剩余坦克数量：%s" % len(MainGame.enemyTankList)), (10, 6))
            # 放置我方坦克
            MainGame.myTank.display_tank()
            # 循环放置敌方坦克
            self.blit_enemy_tank()
            # 循环展示我方子弹
            self.blit_my_bullet()
            # 我方坦克移动
            if not MainGame.myTank.stop:
                MainGame.myTank.move()

            # 显示子弹
            # bullet = Bullet(MainGame.myTank)
            # bullet.display_bullet()
            # 主窗口循环
            pygame.display.update()

    # 循环创建敌方坦克
    def create_enemy_tank(self):
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0, WIN_WIDTH)
            top = random.randint(0, int(WIN_HEIGHT/2))
            speed = random.randint(1, 4)

            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)

    # 循环展示敌方坦克
    def blit_enemy_tank(self):

        for enemy in MainGame.enemyTankList:
            enemy.display_tank()
            enemy.rand_move()

    # 循环展示我方子弹
    def blit_my_bullet(self):
        for myBullet in MainGame.myBulletList:
            # 判断子弹是否存活
            if myBullet.live:
                # 显示
                myBullet.display_bullet()
                # 移动
                myBullet.move()
            else:
                # 删除子弹
                MainGame.myBulletList.remove(myBullet)


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
                # 按空格或者x键发射子弹000
                elif event.key == pygame.K_SPACE or event.key == pygame.K_x:
                    # 创建我方子弹并加入我方子弹列表
                    # if len(MainGame.myBulletList) < MainGame.myBulletCount:
                    myBullet = Bullet(MainGame.myTank)
                    MainGame.myBulletList.append(myBullet)

            # 键位抬起
            if event.type == pygame.KEYUP:
                # 如果是方向键抬起，停止坦克移动
                # if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or \
                #         event.key == pygame.K_RIGHT:
                #     MainGame.myTank.stop = True
                if event.key == self.keyLast:
                    MainGame.myTank.stop = True


class Tank(object):

    def __init__(self):
        pass


class MyTank(Tank):

    def __init__(self, left, top):
        super().__init__()

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


class EnemyTank(Tank):

    def __init__(self, left, top, speed):
        super().__init__()

        # load()返回surface对象
        self.images = {
            "U": pygame.image.load("img/enemy_tankU.gif"),
            "R": pygame.image.load("img/enemy_tankR.gif"),
            "D": pygame.image.load("img/enemy_tankD.gif"),
            "L": pygame.image.load("img/enemy_tankL.gif")
        }

        # 设置初始方向, 随机生成
        self.direction = self.random_direction()
        # 根据方向获取图片
        self.image = self.images[self.direction]
        # 获取图片区域
        self.rect = self.image.get_rect()
        # 设置区域初始位置
        self.rect.left = left
        self.rect.top = top
        # 设置初始速度
        self.speed = speed
        # 设置开关状态
        self.stop = False
        # 设置移动步数
        self.step = 60

    # 获得随机方向
    def random_direction(self):

        direction = None
        num = random.randint(1, 4)

        if num == 1:
            direction = 'U'
        elif num == 2:
            direction = 'D'
        elif num == 3:
            direction = 'L'
        elif num == 4:
            direction = 'R'

        return direction

    def display_tank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)

    # 敌方坦克移动，到达边界时转向，且步数增加20
    def move(self):

        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.direction = self.random_direction()
                self.step += 20
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WIN_WIDTH:
                self.rect.left += self.speed
            else:
                self.direction = self.random_direction()
                self.step += 20
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WIN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.direction = self.random_direction()
                self.step += 20
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.direction = self.random_direction()
                self.step += 20

    # 设置敌方坦克随机移动
    def rand_move(self):

        # 步数减至0时转向，且重置步数
        if self.step <= 0:
            self.direction = self.random_direction()
            self.step = random.randint(30, 60)
        else:
            # 坦克移动，步数递减
            self.move()
            self.step -= 1


class Bullet(object):

    def __init__(self, tank):
        # 加载子弹图像
        self.image = pygame.image.load('img/my_bullet.gif')
        # 坦克方向决定子弹方向
        self.direction = tank.direction
        # 获取区域
        self.rect = self.image.get_rect()
        # 子弹初始位置
        if self.direction == 'U':
            self.rect.left = tank.rect.left + int(tank.rect.width/2-self.rect.width/2)
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + int(tank.rect.width/2-self.rect.width/2)
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + int(tank.rect.height/2-self.rect.height/2)
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + int(tank.rect.height/2-self.rect.height/2)
        # 子弹速度
        self.speed = 8
        # 子弹是否存活，如不存活，则不显示
        self.live = True

    # 显示子弹
    def display_bullet(self):
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)

    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < WIN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < WIN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False


class EnemyBullet(Bullet):

    def __init__(self, tank):
        super().__init__(tank)

        self.image = pygame.image.load('img/enemy_bullet.gif')




if __name__ == '__main__':
    MainGame().start_game()