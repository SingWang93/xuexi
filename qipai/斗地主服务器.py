import random
from socket import *
from time import sleep
from multiprocessing import Pool
# 创建流式套接字
sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定ＩＰ端口
sockfd.bind(('127.0.0.1', 8867))

# 设置监听套接字，创建监听队列
sockfd.listen(5)
c, addr = sockfd.accept()
print("connect from", addr)

d = {}
# 发送规范   地主　服务器　出牌　房间号码　发到某人　内容
sf = "地主^服务器^出牌^"


class Fangjian():

    def __init__(self, s,):  # 初始化实例，name为房间号，设置位置代号用于联通上级服务器，调用洗发牌方法
        self.name = s
        self.wei1 = "0"
        self.wei2 = "1"
        self.wei3 = "2"
        self.fen = 0
        self.fen1 = 0
        self.fen2 = 0
        self.fen3 = 0
        self.dizhuming = ""
        self.gong = ""
        self.gangchupai = ""
        self.pai1 = ""
        self.pai2 = ""
        self.pai3 = ""
        self.xifapai()

    def xifapai(self):  # 洗牌发牌，发请0位置抢地主，积分为0
        lz = []
        l0 = ["0" + str(x) for x in range(3, 10)]
        l1 = [str(x) for x in range(10, 16)] + l0
        l2 = ["ht", "fk", "ho", "mh"]
        l3 = [x + y for x in l2 for y in l1]
        lzong = l3 + ["bj16", "bj17"]
        random.shuffle(lzong)
        print(lzong)
        s1 = "^".join(lzong[:17])
        self.pai1 = s1
        s2 = "^".join(lzong[17:34])
        self.pai2 = s2
        s3 = "^".join(lzong[34:51])
        self.pai3 = s3
        self.gong = "^".join(lzong[51:])

        print(self.gong)
        c.send((sf + self.name + "^" + self.wei1 + "^" + s1 + "信息间隔").encode())
        c.send((sf + self.name + "^" + self.wei2 + "^" + s2 + "信息间隔").encode())
        c.send((sf + self.name + "^" + self.wei3 + "^" + s3 + "信息间隔").encode())

        self.qiangdizhu("0", 0)

    def qiangdizhu(self, s, n):  # 传入要几号位置抢地主，和现在的积分，方法将按照信息发送消息
        c.send((sf + self.name + "^" + s + "^请抢地主" +
                "^" + str(n) + "信息间隔").encode())

# 传入几号位置，积分多少，名字什么，方法将判断是否以及完成抢地主，如没完成是要发下家请求，还是重新洗发牌
    def qiangdizhu2(self, s, n, ming):
        print(self.fen)
        print(9999)
        if s == "0":
            self.fen1 = n
        elif s == "1":
            self.fen2 = n
        elif s == "2":
            self.fen3 = n

        if n > self.fen:
            self.fen = n
            self.dizhuming = ming
            print(self.fen, "改")
        if s == "0":
            if self.fen < 3:
                self.qiangdizhu("1", self.fen)
            else:
                self.fadizhupai()
        if s == "1":
            if self.fen < 3:
                self.qiangdizhu("2", self.fen)
            else:
                self.wei1, self.wei2, self.wei3 = self.wei2, self.wei3, self.wei1
                self.pai1, self.pai2, self.pai3 = self.pai2, self.pai3, self.pai1
                self.fadizhupai()
        if s == "2":
            print(self.fen)
            if self.fen == 0:
                self.xifapai()
            else:
                if self.fen == self.fen2:
                    self.wei1, self.wei2, self.wei3 = self.wei2, self.wei3, self.wei1
                    self.pai1, self.pai2, self.pai3 = self.pai2, self.pai3, self.pai1
                    self.fadizhupai()
                elif self.fen == self.fen3:
                    self.wei1, self.wei2, self.wei3 = self.wei3, self.wei1, self.wei2
                    self.pai1, self.pai2, self.pai3 = self.pai3, self.pai1, self.pai2
                    self.fadizhupai()
                elif self.fen == self.fen1:
                    self.wei1, self.wei2, self.wei3 = self.wei1, self.wei2, self.wei3
                    self.fadizhupai()

    def fadizhupai(self):  # 发给三家地主牌是什么
        #     connfd2.send(("地主名^"+name+"^"+str(n)+"^" + s4+"^下家").encode())

        c.send((sf + self.name + "^" + self.wei1 + "^地主名^" + self.dizhuming +
                "^" + str(self.fen) + "^" + self.gong + "^本人" + "信息间隔").encode())

        c.send((sf+self.name+"^"+self.wei2+"^地主名^"+self.dizhuming +
                "^"+str(self.fen)+"^" + self.gong+"^上家"+"信息间隔").encode())

        c.send((sf+self.name+"^"+self.wei3+"^地主名^"+self.dizhuming +
                "^"+str(self.fen)+"^" + self.gong+"^下家"+"信息间隔").encode())

        c.send((sf+self.name+"^"+self.wei1+"^" +
                self.pai1+"^"+self.gong+"信息间隔").encode())
        self.fasuibchu()

    def fasuibchu(self):  # 发送随便出牌
        c.send((sf+self.name+"^"+self.wei1+"^随便出牌"+"信息间隔").encode())

    def fayaodachu1(self):  # 发送要大出牌
        c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())

    def fayaodachu2(self):  # 发送当已经有一个人过后打，要大出牌
        c.send((sf+self.name+"^"+self.wei3+"^位置三要大出牌"+"信息间隔").encode())

    def weizhichu1(self, lx):  # 发送位置0出牌打牌，给其他人
        c.send((sf+self.name+"^"+self.wei2+"^上家出牌^"+"^".join(lx)+"信息间隔").encode())
        c.send((sf+self.name+"^"+self.wei3+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
        if lx[-1] != "0":
            # self.fayaodachu1()
            c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
            return self

    def weizhichu2(self, lx):  # 发送位置１出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei3+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1+"^下家过"+"信息间隔").encode())
            self.fayaodachu2()
            return self
        else:
            c.send((sf+self.name+"^"+self.wei3 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3 = self.wei2, self.wei3, self.wei1
            if lx[-1] != "0":
                c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
                return self

    def weizhichu3(self, lx):  # 发送位置２出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei1+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2+"^下家过"+"信息间隔").encode())
            self.fasuibchu()
            return self
        else:
            c.send((sf+self.name+"^"+self.wei1 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3 = self.wei3, self.wei1, self.wei2
            if lx[-1] != "0":
                c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())
                return self


def chuli(s, fj):

    if fj[2] == "抢地主":  # 抢地主，身分，基分,mingzi
        s.qiangdizhu2(fj[3], int(fj[4]), fj[5])
        print(s.fen, "方法后")
    if fj[2] == "位置一出牌":  # 位置一出牌，出的打牌
        s = s.weizhichu1(fj[3:])
    if fj[2] == "位置二出牌":  # 位置二出牌，出的打牌
        s = s.weizhichu2(fj[3:])
    if fj[2] == "位置三出牌":  # 位出牌，出的打牌
        s = s.weizhichu3(fj[3:])

    return s


pool = Pool(processes=10)

while True:
    f = c.recv(1024)
    fj = f.decode()
    print(fj)
    if fj == "":
        break
    fj = fj.split("^")
    print(fj)
    if fj[0] == "开房间吧":
        a = Fangjian(fj[1])
        d[fj[1]] = a
    if fj[0] == "出牌":  # 出牌　房间号
        s = d[fj[1]]
        d[fj[1]] = pool.apply(chuli, (s, fj,))
