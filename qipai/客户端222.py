from socket import *
import tkinter as tk
from tkinter import messagebox
import pickle
import time
import sys
new_name = ""
image = None
image_file = None
nameid = ""
sockfd = socket()
sockfd.connect(('127.0.0.1', 8880))

# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from socket import *
from pygame.locals import *
import threading
file_path = './obj/images/'
loading_image = file_path + 'loading.png'
guo = file_path + 'guo.bmp'
backgroundsheng_image = file_path + 'backgroudsheng.png'
backgroundbai_image = file_path + 'backgroudbai.png'
background_image = file_path + 'background.png'
# shengli = file_path+"shengli.png"
shibai = file_path+"shibai.png"
send_image = file_path + 'cp.png'
refuse_image = file_path + 'bc.png'
fen1 = file_path+'fen1.bmp'
fen2 = file_path+'fen2.bmp'
fen3 = file_path+'fen3.bmp'
fen0 = file_path+'fen0.bmp'
dizhu = file_path+'dizhu.png'
pinming = file_path+'pinming.png'
xiaobei = file_path+'xiaobei.bmp'
bei2 = file_path+"bei2.bmp"

# pygame.init()
# screen = pygame.display.set_mode((900, 600), 0, 32)
# loading = pygame.image.load(loading_image).convert()
# guos = pygame.image.load(guo).convert()

# screen.blit(loading, (0, 0))  # 画等待
# pygame.display.update()
# sleep(1)
# background = pygame.image.load(background_image).convert()
# screen.blit(background, (0, 0))  # 画背景

# send_pokers = pygame.image.load(send_image).convert()
# refuse_pokers = pygame.image.load(refuse_image).convert()
# fen1s = pygame.image.load(fen1).convert()
# fen2s = pygame.image.load(fen2).convert()
# fen3s = pygame.image.load(fen3).convert()
# fen0s = pygame.image.load(fen0).convert()
# shenglis = pygame.image.load(shengli).convert()
# shibais = pygame.image.load(shibai).convert()
# dizhus = pygame.image.load(dizhu).convert()
# pinmings = pygame.image.load(pinming).convert()
# xiaobeis = pygame.image.load(xiaobei).convert()
# bei2s = pygame.image.load(bei2).convert()
lzuikai = []
lgongpai = []
shangjiashenfen = ""
xiajiashenfen = ""
benrenshenfen = ""
lshangjia = []
lxiajia = []
lgangchu = []
shangsheng = '17'
xiasheng = '17'
dizhufangjianhao = ""
qianzhui = "地主^客户^出牌^"+dizhufangjianhao
y1 = 0
n = 11  # 10秒倒计时计数
c = ''
tuichu=0

def dizhumain(s):
    pygame.init()
    screen = pygame.display.set_mode((900, 600), 0, 32)
    loading = pygame.image.load(loading_image).convert()
    guos = pygame.image.load(guo).convert()

    screen.blit(loading, (0, 0))  # 画等待
    pygame.display.update()
    sleep(1)
    backgroundsheng=pygame.image.load(backgroundsheng_image).convert()
    backgroundbai=pygame.image.load(backgroundbai_image).convert()
    
    background = pygame.image.load(background_image).convert()
    screen.blit(background, (0, 0))  # 画背景

    send_pokers = pygame.image.load(send_image).convert()
    refuse_pokers = pygame.image.load(refuse_image).convert()
    fen1s = pygame.image.load(fen1).convert()
    fen2s = pygame.image.load(fen2).convert()
    fen3s = pygame.image.load(fen3).convert()
    fen0s = pygame.image.load(fen0).convert()
    # shenglis = pygame.image.load(shengli).convert()
    shibais = pygame.image.load(shibai).convert()
    dizhus = pygame.image.load(dizhu).convert()
    pinmings = pygame.image.load(pinming).convert()
    xiaobeis = pygame.image.load(xiaobei).convert()
    bei2s = pygame.image.load(bei2).convert()
    global lshangjia, lxiajia, lzuikai
    name = s
    d = 0

    def daojishi():  # 倒计时函数，
        global n
        while True:
            n -= 1
            sleep(1)
            if n <= 0:
                break

    def huasheng():  # 绘制剩余牌数字
        myfont = pygame.font.Font(None, 30)
        whit = 255, 255, 255
        shuzi1 = myfont.render(shangsheng, False, whit)
        screen.blit(shuzi1, (50, 300))
        shuzi2 = myfont.render(xiasheng, False, whit)
        screen.blit(shuzi2, (850, 300))

    def daojishihuitu():  # 绘制倒计时
        global n

        myfont = pygame.font.Font(None, 40)
        whit = 0, 0, 255
        if n>0:
            shuzi3 = myfont.render(str(n), False, whit)
            screen.blit(shuzi3, (600, 400))

    def dayin(L, x, y):  # 传入要打印牌扑克的列表，和起始的坐标点,打印出扑克
        for h in L:
            hs = pygame.image.load(file_path+h+".jpg").convert()
            screen.blit(hs, (x, y))
            x += 20

    def greater_than(lzuikai, c):  # 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        while True:
            print("能管上吗?")
            t = threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                # background = pygame.image.load(background_image).convert()
                # screen.blit(background, (0, 0))
                sockfd.send((qianzhui+"^位置二出牌^过").encode())
                global lgangchu
                lgangchu = ["过"]
                print("管不上")
                return
            else:
                if jian2(a, c):
                    print("zhen")
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send(
                        (qianzhui+"^位置二出牌^"+a+"^"+str(sheng)).encode())
                    return


                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("地主^客户^结算一^胜利^"+dizhufangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        dizhushenglihui()
                        return

                else:
                    print("jia")
                    print("输入错误，请重新输入")

    def greater_than2(lzuikai, c):  # 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        while True:
            print("能管上吗?")
            t = threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                # background = pygame.image.load(background_image).convert()
                # screen.blit(background, (0, 0))
                sockfd.send((qianzhui+"^位置三出牌^过").encode())
                print("管不上")
                global lgangchu
                lgangchu = ["过"]
                return
            else:
                if jian2(a, c):
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send(
                        (qianzhui+"^位置三出牌^"+a+"^"+str(sheng)).encode())
                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("地主^客户^结算一^胜利^"+dizhufangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        dizhushenglihui()
                    return

                else:
                    print("输入错误，请重新输入")

    def jian1(a):  # 检测随意出牌,但要符合出牌基本规则
        xinl = paixu(a)
        l = xinl.split("^")
        if len(l) == 2:
            if l == ["bj16", "bj17"]:
                return True
        if len(l) == 1:
            return True
        if len(l) == 2:
            if l[0][2:] == l[1][2:]:
                return True
            return False
        if len(l) == 3:
            if l[0][2:] == l[1][2:] and l[0][2:] == l[2][2:]:
                return True
            return Fals
        if len(l) == 4:
            if (l[0][2:] == l[1][2:] and l[0][2:] == l[2][2:]):
                return True
            if (l[1][2:] == l[2][2:] and l[1][2:] == l[3][2:]):
                return True

        if len(l) > 4:
            f = len(l)
            b = int(l[0][2:])
            for x in range(f):
                if int(l[x][2:]) != b + x:
                    return False
            return True

        return True

    def gaishuju(dazong):  # 收到抢地主信息，改３家的身份，和地主的牌数，和公共牌
        global lzuikai, lgongpai, shangjiashenfen, xiajiashenfen, benrenshenfen
        lshuju = dazong.split("^")
        dizhuname = lshuju[1]
        lgongpai = lshuju[3:-1]
        if lshuju[-1] == "本人":
            # lzuikai = (lzuikai+lshuju[3:-1]).copy

            print(lzuikai)
        if lshuju[-1] == "本人":
            shangjiashenfen = "贫民"
            xiajiashenfen = "贫民"
            benrenshenfen = "地主"
        if lshuju[-1] == "上家":
            shangjiashenfen = "地主"
            xiajiashenfen = "贫民"
            benrenshenfen = "贫民"
            global shangsheng
            shangsheng = "20"
        if lshuju[-1] == "下家":
            shangjiashenfen = "贫民"
            xiajiashenfen = "地主"
            benrenshenfen = "贫民"
            global xiasheng
            xiasheng = "20"

    def click(lzuikai):  # 鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回空
        # screen.blit(send_pokers, (610, 250))
        # screen.blit(refuse_pokers, (610, 330))
        global n,ncun
        print(99999)
        n=ncun
        n1 = n
        print(n1)
        print(n)
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260 + len(a3) * 20) and y in range(430, 581):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + len(a3) * 20 + 85) and y in range(430, 581):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(610, 661) and y in range(250, 291):
                            print(L1, '22222')

                            ncun=n
                            n=0
                            return L1
                        elif x in range(610, 661) and y in range(330, 371):
                            n = 0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1 != n:
                n1 = n
                move_poker(L1, lzuikai)
            if n < 1:
                return []

    def click2(lzuikai):  # 鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回地一个扑克
        # screen.blit(send_pokers, (610, 250))
        # screen.blit(refuse_pokers, (610, 330))
        global n
        print(99999)
        n1 = n
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260 + len(a3) * 20) and y in range(430, 581):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + len(a3) * 20 + 85) and y in range(430, 581):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(610, 661) and y in range(250, 291):
                            print(L1, '22222')
                            n = 0
                            return L1
                        elif x in range(610, 661) and y in range(330, 371):
                            n = 0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1 != n:
                n1 = n
                move_poker(L1, lzuikai)
            if n < 1:
                print(a3[0])
                L1 = []
                L1.append(a3[0])
                return L1

    def move_poker(L1, lzuikai):  # 打印出点鼠标后，扑克的新顺序
        # screen.blit(background, (0, 0))
        # screen.blit(xiaobeis, (0, 200))
        # screen.blit(xiaobeis, (800, 200))
        huasheng()
        # huayichupai2()
        screen.blit(bei2s, (0, 400))
        screen.blit(send_pokers, (610, 250))
        screen.blit(refuse_pokers, (610, 330))
        daojishihuitu()
        if benrenshenfen != "":
            if shangjiashenfen == "地主":
                screen.blit(dizhus, (0, 0))
            else:
                screen.blit(pinmings, (0, 0))
            if xiajiashenfen == "地主":
                screen.blit(dizhus, (800, 0))
            else:
                screen.blit(pinmings, (800, 0))
            if benrenshenfen == "地主":
                screen.blit(dizhus, (40, 440))
            else:
                screen.blit(pinmings, (40, 440))
        x1 = 0
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                win_lose(u"YOU WIN!!!")
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            if poker2 in L1:
                sa = 400
            else:
                sa = 430
            screen.blit(poker_outhand, (260 + x1, sa))
            x1 += 20
        # sleep(0.01)
        pygame.display.update()

    def informal(name, lzuikai):  # 随意出牌
        print("随便出")
        while True:
            t = threading.Thread(target=daojishi)
            t.start()
            L1 = click2(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a != "":
                if jian1(a):
                    chuqu(lzuikai, a)
                    global lgangchu
                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    background = pygame.image.load(
                        background_image).convert()
                    screen.blit(background, (0, 0))
                    for poker2 in l1:
                        poker_outhand = pygame.image.load(
                            file_path + poker2 + '.jpg').convert_alpha()
                        screen.blit(poker_outhand, (250 + x1, 300))
                        x1 += 20
                        # sleep(0.01)
                        # pygame.display.update()
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    print(lzuikai)
                    sheng = len(lzuikai)
                    sockfd.send(
                        (qianzhui+"^位置一出牌^"+'^'.join(L1)+"^"+str(sheng)).encode())



                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("地主^客户^结算一^胜利^"+dizhufangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        dizhushenglihui()

                    return
                else:
                    print("输入错误，请重新输入")
            else:
                print('输入错误，请重新输入')

    def hou(str1):  # 取后两位数字，用于排序
        if str1 == '':
            return
        return int(str1[2:])

    def huayichupai():  # 画已经出的牌（包括，上家，下家，和自己）

        # 上家出牌
        print(lshangjia)
        print(lxiajia)
        print(lgangchu)
        if lshangjia == []:
            pass
        elif lshangjia == ["过"]:
            screen.blit(guos, (225, 225))
        else:

            dayin(lshangjia, 130, 160)

        if lxiajia == []:
            pass
        elif lxiajia == ["过"]:
            screen.blit(guos, (678, 225))
        else:
            dayin(lxiajia, 700, 160)

        if lgangchu == []:
            pass
        elif lgangchu == ["过"]:
            screen.blit(guos, (260, 300))
        else:
            dayin(lgangchu, 300, 250)

        if lgongpai == []:
            pass
        else:

            dayin(lgongpai, 400, 0)

    def huayichupai2():  # （包括，上家，下家）

        # 上家出牌
        print(lshangjia)
        print(lxiajia)
        print(lgangchu)
        if lshangjia == []:
            pass
        elif lshangjia == ["过"]:
            screen.blit(guos, (225, 225))
        else:

            dayin(lshangjia, 130, 160)

        if lxiajia == []:
            pass
        elif lxiajia == ["过"]:
            screen.blit(guos, (678, 225))
        else:
            dayin(lxiajia, 700, 160)

        if lgongpai == []:
            pass
        else:

            dayin(lgongpai, 400, 0)

    def refresh(lzuikai):  # 全图刷新
        screen.blit(background, (0, 0))

        screen.blit(xiaobeis, (0, 200))
        screen.blit(xiaobeis, (800, 200))
        huasheng()
        huayichupai()
        if benrenshenfen != "":
            if shangjiashenfen == "地主":
                screen.blit(dizhus, (0, 0))
            else:
                screen.blit(pinmings, (0, 0))
            if xiajiashenfen == "地主":
                screen.blit(dizhus, (800, 0))
            else:
                screen.blit(pinmings, (800, 0))
            if benrenshenfen == "地主":
                screen.blit(dizhus, (40, 440))
            else:
                screen.blit(pinmings, (40, 440))

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':

                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 430))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()
    def dizhushenglihui():
        screen.blit(background, (0, 0))
        screen.blit(xiaobeis, (0, 200))
        screen.blit(xiaobeis, (800, 200))
        huasheng()
        huayichupai()
        myfont = pygame.font.Font(None, 130)
        whit = 255, 0, 0
        shenglizi = myfont.render("win", False, whit)
        screen.blit(shenglizi, (300, 200))



        if benrenshenfen != "":
            if shangjiashenfen == "地主":
                screen.blit(dizhus, (0, 0))
            else:
                screen.blit(pinmings, (0, 0))
            if xiajiashenfen == "地主":
                screen.blit(dizhus, (800, 0))
            else:
                screen.blit(pinmings, (800, 0))
            if benrenshenfen == "地主":
                screen.blit(dizhus, (40, 440))
            else:
                screen.blit(pinmings, (40, 440))

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':

                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 430))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()
        sleep(10)
        pygame.quit()

    def dizhushengshibaihui():
        screen.blit(background, (0, 0))
        screen.blit(xiaobeis, (0, 200))
        screen.blit(xiaobeis, (800, 200))
        huasheng()
        huayichupai()

        myfont = pygame.font.Font(None, 130)
        whit = 255, 0, 0
        shenglizi = myfont.render("failure", False, whit)
        screen.blit(shenglizi, (300, 200))


        if benrenshenfen != "":
            if shangjiashenfen == "地主":
                screen.blit(dizhus, (0, 0))
            else:
                screen.blit(pinmings, (0, 0))
            if xiajiashenfen == "地主":
                screen.blit(dizhus, (800, 0))
            else:
                screen.blit(pinmings, (800, 0))
            if benrenshenfen == "地主":
                screen.blit(dizhus, (40, 440))
            else:
                screen.blit(pinmings, (40, 440))

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':

                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 430))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()
        sleep(10)
        pygame.quit()

    def jiaofen0():  # 叫地主事件　如果上次叫分积分0触发
        screen.blit(fen1s, (200, 300))
        screen.blit(fen2s, (350, 300))
        screen.blit(fen3s, (500, 300))
        screen.blit(fen0s, (650, 300))
        # screen.blit(refuse_pokers, (610, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(200, 300) and y in range(300, 350):
                            return 1
                        elif x in range(350, 450) and y in range(300, 350):
                            return 2
                        elif x in range(500, 600) and y in range(300, 350):
                            return 3
                        elif x in range(650, 750) and y in range(300, 350):
                            return 0
                    except:
                        continue

    def jiaofen1():  # 叫地主事件　如果上次叫分积分１触发
        # screen.blit(fen1s, (200, 300))
        screen.blit(fen2s, (350, 300))
        screen.blit(fen3s, (500, 300))
        screen.blit(fen0s, (650, 300))
        # screen.blit(refuse_pokers, (610, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(350, 450) and y in range(300, 350):
                            return 2
                        elif x in range(500, 600) and y in range(300, 350):
                            return 3
                        elif x in range(650, 750) and y in range(300, 350):
                            return 0
                    except:
                        continue

    def jiaofen2():  # 叫地主事件　如果上次叫分积分２触发
        # screen.blit(fen1s, (200, 300))
        # screen.blit(fen2s, (350, 300))
        screen.blit(fen3s, (500, 300))
        screen.blit(fen0s, (650, 300))
        # screen.blit(refuse_pokers, (610, 330))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(500, 600) and y in range(300, 350):
                            return 3
                        elif x in range(650, 750) and y in range(300, 350):
                            return 0
                    except:
                        continue

    def paixu(a):  # 把字符串根据后两位数字排序
        lp = a.split("^")
        xinl = sorted(lp, key=hou)
        xina = "^".join(xinl)
        return xina

    def jianzhadan(a):  # 检测是否炸弹
        l1 = paixu(a).split("^")
        if len(l1) == 4:
            if l1[0][2:] == l1[1][2:] == l1[2][2:] == l1[3][2:]:
                return True
        return False

    def jian2(a, b):  # 检测是否符合基本出牌原则,是否比上一家大
        if not jian1(a):
            return False
        l1 = paixu(a).split("^")
        l2 = paixu(b).split("^")
        if l1 == ["bj16", "bj17"]:
            return True
        if l2 == ["bj16", "bj17"]:
            return False
        if jianzhadan(a) == True and \
                jianzhadan(b) == False:
            return True
        if jianzhadan(a) == False and \
                jianzhadan(b) == True:
            return False
        if jianzhadan(a) == True and jianzhadan(b) == True:
            if l1[0][2:] > l2[0][2:]:
                return True
            return False

        if len(l1) == 1 and len(l2) == 1:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == 2 and len(l2) == 2:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == 3 and len(l2) == 3:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == 4 and len(l2) == 4:
            l1xiao = [x[2:] for x in l1]
            l2xiao = [x[2:] for x in l2]
            for x in l1xiao:
                if l1xiao.count(x) == 3:
                    zhi1 = x
            for x in l2xiao:
                if l2xiao.count(x) == 3:
                    zhi2 = x
            if int(zhi1) > int(zhi2):
                return True
            return False
        if len(l1) == len(l2) and len(l1) > 4:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        return False

    def chuqu(lzuikai, a):  # 将列表中已出的牌删除
        l1 = a.split("^")
        for x in l1:
            if x in lzuikai:
                lzuikai.remove(x)

    def qiangdizhu(name, dazong):  # 根据收到信息，判断应该调用那个叫分函数
        lq = dazong.split("^")
        n = int(lq[1])
        if n == 0:
            nxin = jiaofen0()
        elif n == 1:
            nxin = jiaofen1()
        elif n == 2:
            nxin = jiaofen2()
        sockfd.send((qianzhui+'^抢地主^'+(str(nxin))+"^"+nameid).encode())
    while True:
        global tuichu
        if tuichu==1:
            break
        d = 99
        global n,ncun
        n = 30
        ncun=n
        data = sockfd.recv(1024)
        if data == "":
            print(9999)
        dax = data.decode()
        daxf = dax.split("信息间隔")
        for x in daxf:
            dazong = x
            jiezong = dazong.split("^")
            if dazong == "":
                pass
            else:
                if dazong == "上家过":
                    lshangjia = ["过"]
                if dazong == "下家过":
                    lxiajia = ["过"]
                print(data.decode())
                if dazong == "随便出牌":
                    informal(name, lzuikai)
                    if len(lzuikai)==0:
                        return
                elif dazong == "位置二要大出牌":
                    greater_than(lzuikai, c)
                    if len(lzuikai)==0:
                        return
                elif dazong == "位置三要大出牌":
                    greater_than2(lzuikai, c)
                    if len(lzuikai)==0:
                        return
                elif dazong[:4] == "请抢地主":
                    qiangdizhu(name, dazong)
                elif dazong[:3] == "地主名":
                    gaishuju(dazong)
                    print("已经显示地主了")

                elif dazong[:4] == "上家出牌":
                    s2 = dazong.split("^")
                    global  shangsheng
                    c = "^".join(s2[1:-1])
                    lshangjia = s2[1:-1]
                    shangsheng = s2[-1]
                elif dazong[:4] == "下家出牌":
                    s2 = dazong.split("^")
                    global xiasheng
                    c = "^".join(s2[1:-1])
                    lxiajia = s2[1:-1]
                    xiasheng = s2[-1]
                elif dazong=="上家胜利":
                    if  benrenshenfen==shangjiashenfen:
                        dizhushenglihui()
                        return
                    else:
                        dizhushengshibaihui()
                        return
                elif dazong=="下家胜利":
                    if  benrenshenfen==xiajiashenfen:
                        dizhushenglihui()
                        return
                    else:
                        dizhushengshibaihui()
                        return




                else:
                    b = dazong
                    if b[:2] in ["ht", "fk", "ho", "mh", "bj"]:
                        if len(b.split("^")) > 16:
                            sp = paixu(b)
                            lzuikai = b.split("^")
                refresh(lzuikai)

        # print(1)
        # refresh(lzuikai)




















npao=30

def paodemain(nameid):#跑对快主函数
    qianzhui = "跑得快^客户^出牌^"+paodekfangjianhao
    pygame.init()
    file_path = './obj/images1/' #图片路径
    loading_image = file_path + 'loading.png' #加载图片初始化
    background_image = file_path + 'background.bmp' #背景图
    cp_image = file_path + 'cp.png'  #出牌
    bu_image = file_path + 'bc.png' #不出
    background1 = file_path+"background1.bmp" #刷新牌背景
    shengli_image=file_path+"shengli.png"
    shibai_image =file_path + "shibai.png"
    #生成主屏幕screen,第一个参数表示屏幕大小;第二个0表示不使用特性,使用时用
    #pygame.display.flip()来刷新屏幕;32表示色深; 
    pygame.init()
    screen = pygame.display.set_mode((900, 600), 0, 32)#生成窗口
    #.load(图片路径) .convert()将图片处理为surface对象
    loading = pygame.image.load(loading_image).convert()
    screen.blit(loading, (0, 0))  # 画等待
    pygame.display.update()
    sleep(1)
    background = pygame.image.load(background_image).convert()
    screen.blit(background, (0, 0))  # 画背景
    cp_pokers = pygame.image.load(cp_image).convert()
    bu_pokers = pygame.image.load(bu_image).convert()

    shenglis = pygame.image.load(shengli_image).convert()
    shibais=pygame.image.load(shibai_image).convert()
    # shibais = pygame.image.load(shibai_image).convert()

    background1s = pygame.image.load(background1).convert()
    lzuikai = []
    lgongpai = []
    # shangjiashenfen = ""
    # xiajiashenfen = " = "
    lshangjia = []
    lduijia =[]
    lxiajia = []
    lgangchu = []
    buyao = 'pass'
    shangsheng = '10'
    xiasheng = '10'
    duisheng='10'
    n=30#30秒倒计时计数

    def daojishi():#倒计时函数，
        global npao
        while True:
            npao-=1
            sleep(1)
            if npao<=0:
                break
    def huasheng():  # 绘制剩余牌数字
        myfont = pygame.font.Font(None, 30)#字号
        color = 0, 0, 0 
        # 把字符转化成图像
        shuzi1 = myfont.render(shangsheng, False, color) #上家
        #把图片绘制在指定位置
        screen.blit(shuzi1, (75,365))

        shuzi2 = myfont.render(xiasheng, False, color) #下家
        screen.blit(shuzi2, (830, 365))

        shuzi3 = myfont.render(duisheng, False, color) #对家
        screen.blit(shuzi3, (545, 175))

    def daojishihuitu():#绘制倒计时
        global npao

        myfont = pygame.font.Font(None, 40)
        color = 0, 0, 255
        if npao <= 10:
            color = 255, 0, 0
        #本家
        if npao>0:
            benjia = myfont.render(str(npao), False, color)
            screen.blit(benjia,(150,500))

    def dayin(L, x, y):  # 传入要打印牌扑克的列表，和起始的坐标点,打印出扑克
        for h in L:
            hs = pygame.image.load(file_path+h+".jpg").convert()
            screen.blit(hs, (x, y))
            x += 20

    def greater_than(lzuikai, c):# 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        nonlocal lgangchu
        while True:
            print("能管上吗?")
            t=threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                sockfd.send((qianzhui+"^位置二出牌^过").encode())

                lgangchu = ["过"]
                print("管不上")
                return
            else:
                if jian2(a, c):
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    print('管上')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send((qianzhui+"^位置二出牌^"+a+"^"+str(sheng)).encode())
                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("跑得快^客户^结算一^胜利^"+paodefangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        paodekshenglihui()
                    return
                else:
                    print("输入错误，请重新输入")



    def greater_than3(lzuikai, c):# 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        nonlocal lgangchu
        while True:
            print("能管上吗?")
            t=threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                sockfd.send((qianzhui+"^位置四出牌^过").encode())

                lgangchu = ["过"]
                print("管不上")
                return
            else:
                if jian2(a, c):
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    print('管上')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send((qianzhui+"^位置四出牌^"+a+"^"+str(sheng)).encode())
                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("跑得快^客户^结算一^胜利^"+paodefangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        paodekshenglihui()
                    return
                else:
                    print("输入错误，请重新输入")
    def greater_than2(lzuikai, c):# 传入手拍列表，和上次人出牌，请玩家在手中选择，比上次牌大的，或者跳过不出牌
        nonlocal lgangchu
        while True:
            print("能管上吗?")
            t=threading.Thread(target=daojishi)
            t.start()
            L1 = click(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a == '':
                sockfd.send((qianzhui+"^位置三出牌^过").encode())

                lgangchu = ["过"]
                print("管不上")
                return
            else:
                if jian2(a, c):
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    print('管上')
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    sheng = len(lzuikai)
                    sockfd.send((qianzhui+"^位置三出牌^"+a+"^"+str(sheng)).encode())
                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(
                            ("跑得快^客户^结算一^胜利^"+paodefangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        paodekshenglihui()
                    return
                else:
                    print("输入错误，请重新输入")

    def jian1(a):  # 检测随意出牌,但要符合出牌基本规则
        L = paixu(a)
        nL = L.split("^")
        if len(nL) == 1: #出牌数为1
            return True
        if len(nL) == 2: #出牌数为2
            if nL[0][2:] == nL[1][2:]:
                return True
            return False
        if len(nL) == 3: #出牌数为3
            if nL[0][2:] != nL[1][2:] != nL[2][2:]:#三张牌不同,但牌值相邻,为顺
                f = len(nL)
                b = int(nL[0][2:])
                for x in range(f):
                    if int(nL[x][2:]) != b + x:
                        return False
                    return True
                return False
        if len(nL) >= 4: #出牌数大于4  牌值相邻为顺
            f = len(nL) 
            b = int(nL[0][2:])
            for x in range(f):
                if int(nL[x][2:]) != b + x:
                    return False
            return True
        return True

    def click(lzuikai): #鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回空

        global npao
        print(99999)
        n1=npao
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260+ len(a3) * 20) and \
                           y in range(470, 591):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + \
                                len(a3) * 20 + 85) and \
                             y in range(470, 591):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            #出牌按钮位置
                        elif x in range(620, 720) and y in \
                            range(460, 500):
                            print(L1, '22222')
                            npao=0
                            return L1
                            #不出按钮位置
                        elif x in range(620, 720) and y in \
                            range(510, 550):
                            npao=0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1!=npao:
                n1=npao
                move_poker(L1, lzuikai)
            if npao<1:
                print("已经返回空")
                return []
    def click2(lzuikai):  # 鼠标事件，点鼠标选择扑克,每秒打印１次倒计时，超时返回地一个扑克
        global npao
        print(99999)
        n1=npao
        pygame.display.update()
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        L1 = []
        move_poker(L1, lzuikai)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                elif event.type == MOUSEBUTTONUP:
                    try:
                        if x in range(260, 260 + len(a3) * 20) and \
                           y in range(470, 591):
                            ss = (x - 260) // 20
                            if a3[ss] in L1:
                                L1.remove(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[ss])
                                print(L1)
                                move_poker(L1, lzuikai)
                        elif x in range(260 + len(a3) * 20, 260 + \
                                len(a3) * 20 + 85) and \
                             y in range(470, 591):
                            if a3[-1] in L1:
                                L1.remove(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                            else:
                                L1.append(a3[-1])
                                print(L1)
                                move_poker(L1, lzuikai)
                        # elif x in range(610, 661) and y in range(250, 291):
                        elif x in range(620, 720) and y in range(460, 500):

                            print(L1, '22222')
                            npao=0
                            return L1
                        elif x in range(620, 720) and y in range(510, 550):
                            npao=0
                            L1 = []
                            return L1
                    except:
                        continue
            if n1!=npao:
                n1=npao
                move_poker(L1, lzuikai)
            if npao<1:
                print(a3[0])
                L1=[]
                L1.append(a3[0])
                return L1

    def move_poker(L1, lzuikai):  # 打印出点鼠标后，扑克的新顺序
        huasheng()
        screen.blit(background1s, (0, 450))
        screen.blit(cp_pokers,(620,460))  #出牌按钮位置
        screen.blit(bu_pokers,(620,510)) #不出按钮位置
        daojishihuitu()
        
        x1 = 0
        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                win_lose(u"YOU WIN!!!")
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            if poker2 in L1:
                sa = 450
            else:
                sa = 470
            screen.blit(poker_outhand, (260 + x1, sa))
           
            x1 += 20
        pygame.display.update()

    def informal(name, lzuikai):  # 随意出牌
        nonlocal lgangchu
        print("随便出")
        while True:
            t=threading.Thread(target=daojishi)
            t.start()
            L1 = click2(lzuikai)
            t.join()
            a = '^'.join(L1)
            if a != "":
                if jian1(a):
                    chuqu(lzuikai, a)

                    lgangchu = L1.copy()

                    x1 = 0
                    l1 = a.split('^')
                    print(l1)
                    background = pygame.image.load(background_image).convert()
                    screen.blit(background, (0, 0))
                    for poker2 in l1:
                        poker_outhand = pygame.image.load(
                            file_path + poker2 + '.jpg').convert_alpha()
                        screen.blit(poker_outhand, (250 + x1, 300))
                        x1 += 20
                        # sleep(0.01)
                        pygame.display.update()
                    print("您剩余牌为", paixu("^".join(lzuikai)))
                    print(lzuikai)
                    sheng = len(lzuikai)
                    sockfd.send((qianzhui+"^位置一出牌^"+'^'.join(L1)+"^"+str(sheng)).encode())
                    if len(lzuikai) == 0:
                        sleep(0.2)
                        sockfd.send(("跑得快^客户^结算一^胜利^"+paodekfangjianhao+"^"+benrenshenfen+"^"+nameid).encode())
                        paodekshenglihui()
                    return
                else:
                    print("输入错误，请重新输入")
            else:
                print('输入错误，请重新输入')


    def hou(str1):  # 取后两位数字，用于排序
        if str1 == '':
            return
        return int(str1[2:])

    def huayichupai():  # 画已经出的牌（包括，上家，下家，和自己）

        print(lshangjia)
        print(lxiajia)
        print(lgangchu)
        print(lduijia)

        passfont = pygame.font.Font(None, 30)#字号
        color = 255, 0, 0 
        # 把字符转化成图像
        pass0 = passfont.render(buyao, False, color) #上家
        pass1 = passfont.render(buyao, False, color) #下家
        pass2 = passfont.render(buyao, False, color) #本家
        pass3 = passfont.render(buyao, False, color) #对家
      
        # 上家出牌
        if lshangjia == []:
            pass
        elif lshangjia == ["过"]:
            #把图片绘制在指定位置        
            screen.blit(pass0, (150,340))
        else:
            dayin(lshangjia,140,280)
      
        # 下家出牌
        if lxiajia == []:
            pass
        elif lxiajia == ["过"]:
            screen.blit(pass1, (730,340))
        else:
            dayin(lxiajia,630,280)
       
        #本家出牌
        if lgangchu == []:
            pass
        elif lgangchu == ["过"]:
            screen.blit(pass2, (310, 430))
        else:
            dayin(lgangchu, 350, 310)

        # 对家出牌
        if lduijia == []:
            pass
        elif lduijia == ["过"]:
            screen.blit(pass3, (500,220))
        else:
            dayin(lduijia,450,220)



    def paodekshenglihui():

        # screen.blit(shenglis, (0, 0))

        # huasheng()
        # huayichupai()

        screen.blit(background, (0, 0))
        huasheng()
        huayichupai()
        myfont = pygame.font.Font(None, 130)
        whit = 255, 0, 0
        shenglizi = myfont.render("win", False, whit)
        screen.blit(shenglizi, (300, 200))

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 470))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()

        sleep(10)
        pygame.quit()
    def paoshibaihui():

        screen.blit(background, (0, 0))
        huasheng()
        huayichupai()
        myfont = pygame.font.Font(None, 130)
        whit = 255, 0, 0
        shenglizi = myfont.render("failure", False, whit)
        screen.blit(shenglizi, (300, 200))


        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 470))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()

        sleep(10)
        pygame.quit()




    def refresh(lzuikai):  # 全图刷新
        screen.blit(background, (0, 0))

        huasheng()
        huayichupai()

        x1 = 0
        print(lzuikai)

        a1 = '^'.join(lzuikai)
        a2 = paixu(a1)
        a3 = a2.split('^')
        for poker2 in a3:
            if poker2 == '':
                break
            poker_outhand = pygame.image.load(
                file_path + poker2 + '.jpg').convert_alpha()
            screen.blit(poker_outhand, (260 + x1, 470))
            x1 += 20
            # sleep(0.01)
        pygame.display.update()

    def paixu(a):  # 把字符串根据后两位数字排序
        lp = a.split("^")
        xinl = sorted(lp, key=hou)
        xina = "^".join(xinl)
        return xina

    def super_zhadan(a):  # 检测是否炸弹
        l1 = paixu(a).split("^")
        if len(l1) == 4:
            if l1[0][2:] == l1[1][2:] == l1[2][2:] == l1[3][2:]:
                return True
        return False

    def zhadan(a):
        l1 = paixu(a).split("^")
        if len(l1) == 3:
            if l1[0][2:] == l1[1][2:] == l1[2][2:]:
                return True
        return False

    def jian2(a, b):  # 检测是否符合基本出牌原则,是否比上一家大
        if not jian1(a):
            return False
        l1 = paixu(a).split("^")
        l2 = paixu(b).split("^")
       
        if super_zhadan(a) == True and \
                super_zhadan(b) == False:
            return True
        if super_zhadan(a) == False and \
                super_zhadan(b) == True:
            return False
        if super_zhadan(a) == True and super_zhadan(b) == True:
            if l1[0][2:] > l2[0][2:]:
                return True
            return False
        if zhadan(a) == True and \
                zhadan(b) == False:
            return True
        if zhadan(a) == False and \
                zhadan(b) == True:
            return False
        if len(l1) == 1 and len(l2) == 1:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == 2 and len(l2) == 2:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == 3 and len(l2) == 3:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        if len(l1) == len(l2) and len(l1) >= 4:
            if int(l1[0][2:]) > int(l2[0][2:]):
                return True
            return False
        return False

    def chuqu(lzuikai, a):  # 将列表中已出的牌删除
        l1 = a.split("^")
        for x in l1:
            if x in lzuikai:
                lzuikai.remove(x)

    def main(s):
        nonlocal lshangjia, lxiajia, lduijia, lzuikai
        name = s
        d = 0
        while True:
            d = 99
            global npao
            npao = 30
            data = sockfd.recv(1024)
            if data == "":
                print(9999)
            dax = data.decode()
            daxf = dax.split("信息间隔")
            for x in daxf:
                dazong = x
                jiezong = dazong.split("^")
                if dazong == "":
                    pass
                else:
                    if dazong == "上家过":
                        lshangjia = ["过"]
                    if dazong == "下家过":
                        lxiajia = ["过"]
                    print(data.decode())
                    if dazong == "随便出牌":
                        informal(name, lzuikai)
                        if len(lzuikai)==0:
                            return
                    elif dazong == "位置二要大出牌":
                        greater_than(lzuikai, c)
                        if len(lzuikai)==0:
                            return
                    elif dazong == "位置三要大出牌":
                        greater_than2(lzuikai, c)
                        if len(lzuikai)==0:
                            return
                    elif dazong == "位置四要大出牌":
                        greater_than3(lzuikai, c)
                        if len(lzuikai)==0:
                            return
                    elif dazong[:4] == "请抢地主":
                        qiangdizhu(name, dazong)
                    elif dazong[:3] == "地主名":
                        gaishuju(dazong)
                        print("已经显示地主了")

                    elif dazong[:4] == "上家出牌":
                        s2 = dazong.split("^")
                        nonlocal  shangsheng
                        c = "^".join(s2[1:-1])
                        lshangjia = s2[1:-1]
                        shangsheng = s2[-1]
                    elif dazong[:4] == "下家出牌":
                        s2 = dazong.split("^")
                        nonlocal xiasheng
                        c = "^".join(s2[1:-1])
                        lxiajia = s2[1:-1]
                        xiasheng = s2[-1]
                    elif dazong[:4] == "对家出牌":
                        s2 = dazong.split("^")
                        nonlocal duisheng
                        c = "^".join(s2[1:-1])
                        lduijia = s2[1:-1]
                        duisheng = s2[-1]
                    elif dazong=="上家胜利":



                        paoshibaihui()
                        return
                    elif dazong=="下家胜利":

                        paoshibaihui()
                        return
                    elif dazong=="对家胜利":

                        paoshibaihui()
                        return




                    else:
                        b = dazong
                        if b[:2] in ["ht", "fk", "ho", "mh", "bj"]:
                            if len(b.split("^")) > 9:
                                sp = paixu(b)
                                lzuikai = b.split("^")
                refresh(lzuikai)
    main(nameid)








































def jinrugongnengxuanze():
    print("1000")
    global image
    global image_file

    print("1001")

    youxixze = tk.Tk()  # 调用模块创建窗口
    youxixze.title("请选择游戏")  # 窗口题目
    youxixze.geometry("960x540")  # 窗口大小
    youxixze.resizable(False, False)
    youxixze.transient()

    def dikuaisuks():  # 地主快速开始
        sockfd.send(("地主^客户^快速开始").encode())
        data = sockfd.recv(1024)
        global dizhufangjianhao, qianzhui
        dizhufangjianhao = data.decode()
        qianzhui = "地主^客户^出牌^"+dizhufangjianhao
        print(dizhufangjianhao)
        youxixze.destroy()
        time.sleep(2)
        dizhumain(nameid)
        jinrugongnengxuanze()

    def dichuangjianfj():
        difang = entry_dichuang.get()
        sockfd.send(("地主^客户^开房间^"+difang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        if jieguo[:4] == "已经创建":
            global dizhufangjianhao, qianzhui
            dizhufangjianhao = difang
            qianzhui = "地主^客户^出牌^"+dizhufangjianhao
            youxixze.destroy()
            dizhumain(nameid)
            jinrugongnengxuanze()
        else:
            tk.messagebox.showerror("error", "对不起已经有同名房间")

    def dijiarufj():
        difang = entry_dijia.get()
        sockfd.send(("地主^客户^进入房间^"+difang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        print(jieguo)
        if jieguo == "已经加入":
            global dizhufangjianhao, qianzhui
            dizhufangjianhao = difang
            qianzhui = "地主^客户^出牌^"+dizhufangjianhao
            youxixze.destroy()
            dizhumain(nameid)
            jinrugongnengxuanze()
        elif jieguo == "已经满人":
            tk.messagebox.showerror("error", "对不起该房间满人")
        else:
            tk.messagebox.showerror("error", "对不起没找到")



    def paokuaisuks():
        sockfd.send(("跑得快^客户^快速开始").encode())
        data = sockfd.recv(1024)
        global paodekfangjianhao, paoqianzhui
        paodekfangjianhao = data.decode()
        paoqianzhui = "地主^客户^出牌^"+paodekfangjianhao
        print(paodekfangjianhao)
        youxixze.destroy()

        paodemain(nameid)
        jinrugongnengxuanze()
        print("1321")
        
        



    def paochuangjianfj():
        paofang = entry_paochuang.get()
        sockfd.send(("跑得快^客户^开房间^"+paofang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        if jieguo[:4] == "已经创建":
            global paodekfangjianhao, paoqianzhui
            paodekfangjianhao = paofang
            paoqianzhui = "地主^客户^出牌^"+paodekfangjianhao
            youxixze.destroy()
            paodemain(nameid)
            jinrugongnengxuanze()
        else:
            tk.messagebox.showerror("error", "对不起已经有同名房间")

    def paojiarufj():
        paofang = entry_paojia.get()
        sockfd.send(("跑得快^客户^进入房间^"+paofang).encode())
        data = sockfd.recv(1024)
        jieguo = data.decode()
        print(jieguo)
        if jieguo == "已经加入":
            global paodekfangjianhao, paoqianzhui
            paodekfangjianhao = paofang
            qianzhui = "地主^客户^出牌^"+paodekfangjianhao
            youxixze.destroy()
            time.sleep(2)
            print(1000)
            paodemain(nameid)
            jinrugongnengxuanze()
        elif jieguo == "已经满人":
            tk.messagebox.showerror("error", "对不起该房间满人")
        else:
            tk.messagebox.showerror("error", "对不起没找到")

    canvas = tk.Canvas(youxixze, width=960, height=540)
    image_file = tk.PhotoImage(file="./tt/xuanzeyouxi/xuanzeyouxi.png")
    youxixze.attributes("-alpha", 0.3)
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    canvas.pack(side="top")


    # 斗地主输入房间号
    entry_dijia = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_dijia.place(x=323, y=418)
    entry_dichuang = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_dichuang.place(x=323, y=353)

    image_fileksksd = tk.PhotoImage(file="./tt/xuanzeyouxi/ksksd.png")
    dizhukuaikai = tk.Button(youxixze,image=image_fileksksd,command=dikuaisuks).place(x=154, y=276)

    image_filecjfjd = tk.PhotoImage(file="./tt/xuanzeyouxi/cjfjd.png")
    dizhuchuangj = tk.Button(youxixze,image=image_filecjfjd,command=dichuangjianfj).place(x=154, y=345)

    image_filejrfjd = tk.PhotoImage(file="./tt/xuanzeyouxi/jrfjd.png")
    dizhujiaru = tk.Button(youxixze,image=image_filejrfjd,command=dijiarufj).place(x=154, y=410)



    # # 跑得快输入房间号
    entry_paojia = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_paojia.place(x=750, y=418)
    entry_paochuang = tk.Entry(youxixze,width=11,font=("黑体",18,"bold"))
    entry_paochuang.place(x=750, y=353)

    image_fileksksp = tk.PhotoImage(file="./tt/xuanzeyouxi/ksksp.png")
    paokuaikai = tk.Button(youxixze,image=image_fileksksp, command=paokuaisuks).place(x=582, y=276)
    image_filecjfjp = tk.PhotoImage(file="./tt/xuanzeyouxi/cjfjp.png")
    paochuangj = tk.Button(youxixze,image=image_filecjfjp, command=paochuangjianfj).place(x=582, y=345)
    image_filejrfjp = tk.PhotoImage(file="./tt/xuanzeyouxi/jrfjp.png")
    paojiaru = tk.Button(youxixze,image=image_filejrfjp, command=paojiarufj).place(x=582, y=410)

    youxixze.mainloop()


def jiance():
    pass


def zhaohuimima():
    pass


def kaiqi():
    global image

    def denglu():
        user = entry_name.get()
        pwd = entry_pwd.get()
        print(user)
        print(pwd)
        sockfd.send(("登录^" + user + "^" + pwd).encode())
        data = sockfd.recv(1024)
        print(data.decode())
        if data.decode() == "True":
            global nameid
            nameid = user
            win.destroy()
            jinrugongnengxuanze()
        else:
            tk.messagebox.showerror("error", message="用户名密码不正确")

    def zhuce():
        def zhucetijiao():
            nn = entry_new_name.get()  # nn 注册的用户名
            np = entry_user_pwd.get()  # np 注册的密码
            npt = entry_user_pwd_two.get()  # npt 再次确认密码
            sjh = entry_user_sjh.get()  # shj 手机号
            nc = entry_user_nc.get()  # nc 昵称
            if len(nn) < 6:
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
            elif len(nn) > 18:
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
            elif " " in nn:
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
            elif nn[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRASUVWXYZ":
                tk.messagebox.showerror("error", "用户名以字母开头，6-18位字符，不能有空格")
                
            elif len(np) <= 5:
                tk.messagebox.showerror("error", "密码长度在6-18位字符")
            elif len(np) > 19:
                tk.messagebox.showerror("error", "密码长度在6-18位字符")  # 两次密码不一致，弹窗提示
            elif np != npt:
                tk.messagebox.showerror("error", "两次密码不一致")

            elif sjh[0] != "1" or len(sjh) != 11:
                tk.messagebox.showerror("error", "手机号输入格式不正确")

            elif len(nc) < 6:
                tk.messagebox.showerror("error", "昵称6-18位字符，不能有空格")
            elif len(nc) > 18:
                tk.messagebox.showerror("error", "昵称6-18位字符，不能有空格")
            elif " " in nc :
                tk.messagebox.showerror("error", "昵称6-18位字符，不能有空格")

            else:
                print("注册" + "^" + nn + "^" + np + "^" + sjh + "^" + nc)
                sockfd.send(("注册" + "^" + nn + "^" + np +
                             "^" + sjh + "^" + nc).encode())
                data = sockfd.recv(1024)
                print(data.decode())
                if data.decode() == "True":
                    tanchuang.destroy()
                    tk.messagebox.showinfo("Congratulations", "恭喜您注册成功")
                    win.destroy()
                    jinrugongnengxuanze()
                else:
                    tk.messagebox.showerror("error", message="用户名密码不正确")
# 注册窗口
        tanchuang = tk.Toplevel(win)
        tanchuang.title("欢迎注册乐游天下")
        tanchuang.geometry("630x400")
        tanchuang.resizable(False, False)
        tanchuang.transient(win)

# 注册窗口配置图片
        canvas = tk.Canvas(tanchuang, width=630, height=400)
        image_file = tk.PhotoImage(file="./tt/zhuce/beijing.png")
        image = canvas.create_image(0, 0, anchor="nw", image=image_file)
        canvas.pack(side="top")

        global new_name

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="用户名").place(x=100, y=10)
        entry_new_name = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_new_name.place(x=254, y=6)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="密　码").place(x=100, y=50)
        entry_user_pwd = tk.Entry(tanchuang,width=21,font=("黑体",13),show="*")
        entry_user_pwd.place(x=254, y=60)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="确认密码").place(x=100, y=90)
        entry_user_pwd_two = tk.Entry(tanchuang,width=21,font=("黑体",13), show="*")
        entry_user_pwd_two.place(x=254, y=115)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="手机号").place(x=100, y=130)
        entry_user_sjh = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_user_sjh.place(x=254, y=170)

        # 注册窗口
        # tk.Label(tanchuang, bg="powderblue", text="昵　称").place(x=100, y=170)
        entry_user_nc = tk.Entry(tanchuang,width=21,font=("黑体",13))
        entry_user_nc.place(x=254, y=226)

        # 用户名检测结果提示框
        # var_jiance = tk.StringVar()
        # var_jiance.set = ""
        # lb3 = tk.Label(tanchuang, textvariable=var_jiance,
                       # width=20, height=1).place(x=201, y=30)

        # btn_jiance = tk.Button(tanchuang, text="检测用户名是否可用", command=jiance)
        # btn_jiance.place(x=400, y=10)

        # 注册按钮
        image_filetjzc = tk.PhotoImage(file="./tt/zhuce/tijiaozhuce.png")
        
        btn_tijiao = tk.Button(tanchuang, text="提交注册",image=image_filetjzc, command=zhucetijiao)
        btn_tijiao.place(x=260, y=300)
        win.mainloop()


# 主窗口
    win = tk.Tk()  # 调用模块创建窗口
    win.title("欢迎来到　乐游天下")  # 窗口题目
    win.geometry("960x540")  # 窗口大小
    win.resizable(False, False)
    # 主窗口插入背景图
    canvas = tk.Canvas(win, width=960, height=540)
    image_file = tk.PhotoImage(file="./tt/denglu/denglu2.png")
    image = canvas.create_image(0, 0, anchor="nw", image=image_file)
    canvas.pack(side="top")
    # 主窗口用户名/密码的提示
    # user = tk.Label(win, text="用户名", bg="palegoldenrod").place(x=450, y=300)
    # pwd = tk.Label(win, text="密　码", bg="palegoldenrod").place(x=350, y=360)
    # 用户名输入框
    entry_name = tk.Entry(win,width=24,font=("黑体",18))
    entry_name.place(x=573, y=238)
    # 密码输入框
    entry_pwd = tk.Entry(win, width=24,font=("黑体",18),show="*")
    entry_pwd.place(x=573, y=317)
    image_filed = tk.PhotoImage(file="./tt/denglu/denglu11.png")
    btn_denglu = tk.Button(win, text="登　录",image=image_filed, command=denglu)
    btn_denglu.place(x=573, y=450)

    image_filez = tk.PhotoImage(file="./tt/denglu/zhuce11.png")
    btn_zhuce = tk.Button(win, text="注　册",image=image_filez, command=zhuce)
    btn_zhuce.place(x=783, y=450)

    # image_filezh = tk.PhotoImage(file="./tt/denglu/zhaohui11.png")
    # btn_sign_up = tk.Button(win, text="找回密码",image=image_filezh, command=zhaohuimima)
    # btn_sign_up.place(x=730, y=470)
    win.mainloop()


kaiqi()