# coding: utf-8

"""
坦克大战GUI
    新增功能
    坦克不能穿墙
    我方坦克与敌方坦克不能互穿
"""

import pygame
import time
import random

from pygame.sprite import Sprite

WIN_WIDTH = 1010
WIN_HEIGHT = 600
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


# 基类
class BaseItem(Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


class MainGame(object):
    window = None
    myTank = None
    # 创建敌方坦克列表
    enemyTankList = []
    # 设置敌方坦克数量
    enemyTankCount = 10
    # 创建我方子弹列表
    myBulletList = []
    # 限制子弹数量
    myBulletCount = 5
    # 创建敌方子弹列表
    enemyBulletList = []
    # 创建爆炸列表
    explodeList = []
    # 创建墙壁列表
    wallList = []

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
        self.create_my_tank()
        # 初始化敌方坦克
        self.create_enemy_tank()
        # 初始化墙壁
        self.create_wall()

        while True:
            time.sleep(0.02)
            # 监听事件
            self.event_mgr()
            # 填充背景色
            MainGame.window.fill(BG_COLOR)
            # 放置字体surface
            MainGame.window.blit(self.get_text_surface("敌方剩余坦克数量：%s" % len(MainGame.enemyTankList)), (10, 6))
            # 展示墙壁
            self.blit_wall()
            # 放置我方坦克
            if MainGame.myTank:
                MainGame.myTank.display_tank()
                # 我方坦克移动
                if not MainGame.myTank.stop:
                    MainGame.myTank.move()
                    # 检测是否撞墙
                    MainGame.myTank.hit_wall()
                    # 检测是否与敌方坦克碰撞
                    MainGame.myTank.hit_enemy_tank()

            else:
                # 坦克重生
                self.create_my_tank()
            # 循环放置敌方坦克
            self.blit_enemy_tank()
            # 循环展示我方子弹
            self.blit_my_bullet()
            # 循环展示敌方子弹
            self.blit_enemy_bullet()
            # 循环展示爆炸效果
            self.blit_explode()

            # 主窗口循环
            pygame.display.update()

    # 创建我方坦克
    def create_my_tank(self):
        MainGame.myTank = MyTank(WIN_WIDTH * 0.5 - 25, WIN_HEIGHT * 0.9 - 25)

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
            if enemy.live:
                enemy.display_tank()
                enemy.rand_move()
                # 检测是否撞墙
                enemy.hit_wall()
                # 检测是否与我方坦克相撞
                if MainGame.myTank:
                    enemy.hit_my_tank()
                # 敌方坦克射击
                enemyBullet = enemy.shot()
                # 如果子弹不为空，将子弹加入敌方子弹列表
                if enemyBullet:
                    MainGame.enemyBulletList.append(enemyBullet)


            else:
                MainGame.enemyTankList.remove(enemy)

    # 循环创建墙壁
    def create_wall(self):

        for i in range(9):
            wall = Wall(i*120, WIN_HEIGHT*0.6)
            MainGame.wallList.append(wall)

    # 循环展示墙壁
    def blit_wall(self):
        for wall in MainGame.wallList:
            if wall.live:
                wall.display_wall()
            else:
                MainGame.wallList.remove(wall)

    # 循环展示我方子弹
    def blit_my_bullet(self):
        for myBullet in MainGame.myBulletList:
            # 判断子弹是否存活
            if myBullet.live:
                # 显示
                myBullet.display_bullet()
                # 移动
                myBullet.move()
                # 判断子弹和敌方坦克是否相撞
                myBullet.bullet_hit_tank()
                # 判断子弹是否击中墙壁
                myBullet.bullet_hit_wall()
            else:
                # 删除子弹
                MainGame.myBulletList.remove(myBullet)

    # 循环展示敌方子弹
    def blit_enemy_bullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            if enemyBullet.live:
                enemyBullet.display_bullet()
                enemyBullet.move()
                enemyBullet.bullet_hit_tank()
                # 检查敌方子弹是否击中墙壁
                enemyBullet.bullet_hit_wall()
            else:
                MainGame.enemyBulletList.remove(enemyBullet)

    # 循环展示爆炸效果
    def blit_explode(self):
        # 遍历爆炸效果列表，循环展示爆炸效果
        for explode in MainGame.explodeList:
            if explode.live:
                explode.display_explode()
            else:
                MainGame.explodeList.remove(explode)


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
            if MainGame.myTank:
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


class Tank(BaseItem):

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
        # 存活状态
        self.live = True
        # 记录上一次的位置
        self.lastLeft = self.rect.left
        self.lastTop = self.rect.top

    def stay(self):
        self.rect.left = self.lastLeft
        self.rect.top = self.lastTop

    def hit_wall(self):

        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                self.stay()



class MyTank(Tank):

    def __init__(self, left, top):
        super().__init__(left, top)

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

        self.lastLeft = self.rect.left
        self.lastTop = self.rect.top

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

    def hit_enemy_tank(self):
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self, enemyTank):
                self.stay()


class EnemyTank(Tank):

    def __init__(self, left, top, speed):
        super().__init__(left, top)

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
        # 记录移动前的位置
        self.lastLeft = self.rect.left
        self.lastTop = self.rect.top

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

    def shot(self):
        num = random.randint(1, 500)
        if num <= 10:
            return EnemyBullet(self)

    def hit_my_tank(self):
        if pygame.sprite.collide_rect(self, MainGame.myTank):
            self.stay()


class Bullet(BaseItem):

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
        self.speed = 10
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

    def bullet_hit_tank(self):

        for enemyTank in MainGame.enemyTankList:
            # 判断敌方坦克是否与子弹相撞
            if pygame.sprite.collide_rect(enemyTank, self):
                self.live = False
                enemyTank.live = False

                explode = Explode(enemyTank)
                MainGame.explodeList.append(explode)

    def bullet_hit_wall(self):

        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                self.live = False
                # 墙壁生命值减1
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False


class EnemyBullet(Bullet):

    def __init__(self, tank):
        super().__init__(tank)

        self.image = pygame.image.load('img/enemy_bullet.gif')

    def bullet_hit_tank(self):

        if MainGame.myTank:
            if pygame.sprite.collide_rect(MainGame.myTank, self):
                # 生成爆炸效果并加到爆炸效果列表
                explode = Explode(MainGame.myTank)
                MainGame.explodeList.append(explode)
                self.live = False
                # MainGame.myTank.live = False
                del MainGame.myTank
                MainGame.myTank = None





class Explode(object):

    def __init__(self, tank):
        # 坦克位置决定爆炸位置
        self.rect = tank.rect

        # 爆炸效果图
        self.images = [
            pygame.image.load('img/explode0.gif'),
            pygame.image.load('img/explode1.gif'),
            pygame.image.load('img/explode2.gif'),
            pygame.image.load('img/explode3.gif'),
            pygame.image.load('img/explode4.gif'),
            pygame.image.load('img/explode-1.gif'),
        ]
        # 初始显示第一张图片
        self.step = -1
        # self.image = self.images[self.step]
        # 是否存活
        self.live = True

    def display_explode(self):

        # 展示爆炸效果图，展示完所有图片后，爆炸效果灭亡
        if self.step < len(self.images):
            MainGame.window.blit(self.images[self.step], self.rect)
            self.step += 1
        else:
            self.live = False


class Wall(BaseItem):

    def __init__(self, left, top):

        # 加载墙壁图片
        self.image = pygame.image.load('img/wall.gif')
        # 获取墙壁区域
        self.rect = self.image.get_rect()
        # 设置墙壁初始位置
        self.rect.left = left
        self.rect.top = top
        # 存活状态
        self.live = True
        # 初始生命值
        self.hp = 3

    def display_wall(self):
        # 加载到主窗口
        MainGame.window.blit(self.image, self.rect)


if __name__ == '__main__':
    MainGame().start_game()