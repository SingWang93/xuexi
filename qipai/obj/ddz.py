import pygame
import os
import sys
import random
from pygame.locals import *
from time import *


d = {'h0': pygame.image.load("images/mh3.jpg"),
     'h1': pygame.image.load("images/ht3.jpg"),
     'h2': pygame.image.load("images/fk3.jpg"),
     'h3': pygame.image.load("images/hot3.jpg"),
     'h4': pygame.image.load("images/mh4.jpg"),
     'h5': pygame.image.load("images/ht4.jpg"),
     'h6': pygame.image.load("images/fk4.jpg"),
     'h7': pygame.image.load("images/hot4.jpg"),
     'h8': pygame.image.load("images/mh5.jpg"),
     'h9': pygame.image.load("images/ht5.jpg"),
     'h10': pygame.image.load("images/fk5.jpg"),
     'h11': pygame.image.load("images/hot5.jpg"),
     'h12': pygame.image.load("images/mh6.jpg"),
     'h13': pygame.image.load("images/ht6.jpg"),
     'h14': pygame.image.load("images/fk6.jpg"),
     'h15': pygame.image.load("images/hot6.jpg"),
     'h16': pygame.image.load("images/mh7.jpg"),
     'h17': pygame.image.load("images/ht7.jpg"),
     'h18': pygame.image.load("images/fk7.jpg"),
     'h19': pygame.image.load("images/hot7.jpg"),
     'h20': pygame.image.load("images/mh8.jpg"),
     'h21': pygame.image.load("images/ht8.jpg"),
     'h22': pygame.image.load("images/fk8.jpg"),
     'h23': pygame.image.load("images/hot8.jpg"),
     'h24': pygame.image.load("images/mh9.jpg"),
     'h25': pygame.image.load("images/ht9.jpg"),
     'h26': pygame.image.load("images/fk9.jpg"),
     'h27': pygame.image.load("images/hot9.jpg"),
     'h28': pygame.image.load("images/mh10.jpg"),
     'h29': pygame.image.load("images/ht10.jpg"),
     'h30': pygame.image.load("images/fk10.jpg"),
     'h31': pygame.image.load("images/hot10.jpg"),
     'h32': pygame.image.load("images/mhj.jpg"),
     'h33': pygame.image.load("images/htj.jpg"),
     'h34': pygame.image.load("images/fkj.jpg"),
     'h35': pygame.image.load("images/hotj.jpg"),
     'h36': pygame.image.load("images/mhq.jpg"),
     'h37': pygame.image.load("images/htq.jpg"),
     'h38': pygame.image.load("images/fkq.jpg"),
     'h39': pygame.image.load("images/hotq.jpg"),
     'h40': pygame.image.load("images/mhk.jpg"),
     'h41': pygame.image.load("images/htk.jpg"),
     'h42': pygame.image.load("images/fkk.jpg"),
     'h43': pygame.image.load("images/hotk.jpg"),
     'h44': pygame.image.load("images/mh1.jpg"),
     'h45': pygame.image.load("images/ht1.jpg"),
     'h46': pygame.image.load("images/fk1.jpg"),
     'h47': pygame.image.load("images/hot1.jpg"),
     'h48': pygame.image.load("images/mh2.jpg"),
     'h49': pygame.image.load("images/ht2.jpg"),
     'h50': pygame.image.load("images/fk2.jpg"),
     'h51': pygame.image.load("images/hot2.jpg"),
     'h52': pygame.image.load("images/sjoker.jpg"),
     'h53': pygame.image.load("images/bjoker.jpg")}


class Doudizhu:
    def __init__(self):
        self.a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                  19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                  36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

    def restart(self):
        random.shuffle(self.a)
        n = random.randint(1, 54)
        b = self.a[:n]
        c = self.a[n:]
        self.a = c+b

    def fapai(self):  # 发牌
        self.player1 = self.a[:17]
        self.player2 = self.a[17:34]
        self.player3 = self.a[34:51]
        self.dipai = self.a[51:]

    def qiangdizhu(self):  # 抢地主
        n = random.randint(1, 3)
        self.dizhu = n  # 定义一个实例属性，赋给地主的序号
        if n == 1:
            self.player1 += self.dipai
        if n == 2:
            self.player2 += self.dipai
        if n == 3:
            self.player3 += self.dipai

    def paixu(self):
        self.player1.sort(reverse=True)
        self.player2.sort(reverse=True)
        self.player3.sort(reverse=True)

    def yingshe(self):
        pokercz = [(0, 'h0'), (1, 'h1'), (2, 'h2'), (3, 'h3'),
                   (4, 'h4'), (5, 'h5'), (6, 'h6'), (7, 'h7'),
                   (8, 'h8'), (9, 'h9'), (10, 'h10'), (11, 'h11'),
                   (12, 'h12'), (13, 'h13'), (14, 'h14'), (15, 'h15'),
                   (16, 'h16'), (17, 'h17'), (18, 'h18'), (19, 'h19'),
                   (20, 'h20'), (21, 'h21'), (22, 'h22'), (23, 'h23'),
                   (24, 'h24'), (25, 'h25'), (26, 'h26'), (27, 'h27'),
                   (28, 'h28'), (29, 'h29'), (30, 'h30'), (31, 'h31'),
                   (32, 'h32'), (33, 'h33'), (34, 'h34'), (35, 'h35'),
                   (36, 'h36'), (37, 'h37'), (38, 'h38'), (39, 'h39'),
                   (40, 'h40'), (41, 'h41'), (42, 'h42'), (43, 'h43'),
                   (44, 'h44'), (45, 'h45'), (46, 'h46'), (47, 'h47'),
                   (48, 'h48'), (49, 'h49'), (50, 'h50'), (51, 'h51'),
                   (52, 'h52'), (53, 'h53')]
        zdpai = dict(pokercz)
        pai1 = ''
        for i in range(len(self.player1)):
            pai1 += zdpai[self.player1[i]]+' '
        pai2 = ''
        for i in range(len(self.player2)):
            pai2 += zdpai[self.player2[i]]+' '
        pai3 = ''
        for i in range(len(self.player3)):
            pai3 += zdpai[self.player3[i]]+' '
        self.player1 = pai1  # 这里要把牌的序列赋给三个玩家的实例属性
        self.player2 = pai2
        self.player3 = pai3


play = Doudizhu()  # 使用这个类时，要挨个使用实例的方法
play.restart()
play.fapai()
play.qiangdizhu()
play.paixu()
play.yingshe()
print('dizhu:', play.dizhu)
print('user1:', play.player1)
print('user2:', play.player2)
print('user3:', play.player3)

# 左上角(322, 390)
# 左下角(322, 430)
# 右上角(414, 390)
# 右下角(414, 430)
# 左上角(480, 390)
# 左下角(480, 430)
# 右上角(575, 390)
# 右下角(575, 430)
# 中点(450, 600)


pygame.init()
pygame.display.set_caption('斗地主')
width, height = 900, 600
bland_surface = pygame.Surface((width, height))
screen = pygame.display.set_mode((width, height))
base_folder = os.path.dirname(__file__)
img_folder = os.path.join(base_folder, 'images')
frist_img = pygame.image.load(os.path.join(img_folder, '100.png')).convert()
background_img = pygame.image.load(os.path.join(img_folder, '1.png')).convert()
chupai = pygame.image.load(os.path.join(img_folder, 'cp.png')).convert()
buchu = pygame.image.load(os.path.join(img_folder, 'bc.png')).convert()
clock = pygame.time.Clock()


class DdzUI():
    def __init__(self):
        self.player1 = play.player1.split(' ')
        self.player2 = play.player2.split(' ')
        self.player3 = play.player3.split(' ')

    def main(self):
        running = True
        while running:
            clock.tick(30)
            screen.blit(background_img, (0, 0))
            self.draw_poker()
            # 处理不同事件
            for event in pygame.event.get():
                # 检查是否关闭窗口
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit = True
                elif event.type == MOUSEBUTTONDOWN:
                    # self.draw_poker(self)
                    self.draw_poker(pygame.mouse.get_pos())
            # self.draw_poker()
            pygame.display.flip()


    def draw_poker(self, *args):
        print(args)
        x = 430-(len(self.player1)//2*20)
        y = 450
        jishu = 0
        while jishu < len(self.player1)-1:
            # print('a')
            try:
                djwz+=(args[0][0]-x)//20
            except:
                djwz=22
            if jishu != djwz:
                screen.blit(d[self.player1[jishu]], (x, y))
            else:
                screen.blit(d[self.player1[jishu]], (x, y-20))
                jishu+=1
            x += 20
            jishu += 1
        screen.blit(chupai,(320,390))
        screen.blit(buchu,(480,390))
    def x_yzhou(self):
        self.draw_poker(x, y)

    def dayin():
        for sy in range(self.player1):
            zuobiao=(x,y)
            screen.blit(d[self.player1[jishu]], zuobiao)
            x += 20
            jishu += 1
        screen.blit(chupai,(320,390))
        screen.blit(buchu,(480,390))



    def draw_poker(self, *args):
        x = 430-(len(self.player1)//2*20)
        y = 450
        jishu = 0
        while jishu < len(self.player1)-1:
            zuobiao=(x,y)
            screen.blit(d[self.player1[jishu]], zuobiao)
            x += 20
            jishu += 1
        screen.blit(chupai,(320,390))
        screen.blit(buchu,(480,390))
DdzUI().main()