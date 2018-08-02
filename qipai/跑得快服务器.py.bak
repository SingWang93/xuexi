import random
from socket import *
from time import sleep
from multiprocessing import Pool
# 创建流式套接字
sockfd = socket(AF_INET, SOCK_STREAM, 0)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 绑定ＩＰ端口
sockfd.bind(('127.0.0.1', 8868))

# 设置监听套接字，创建监听队列
sockfd.listen(5)
c, addr = sockfd.accept()
print("connect from", addr)

d = {}
# 发送规范   地主　服务器　出牌　房间号码　发到某人　内容
sf = "跑得快^服务器^出牌^"


class Fangjian():

    def __init__(self, s):  # 初始化实例，name为房间号，设置位置代号用于联通上级服务器，调用洗发牌方法
        self.name = s
        self.wei1 = "0"
        self.wei2 = "1"
        self.wei3 = "2"
        self.wei4 = "3"
        self.pai1 = ""
        self.pai2 = ""
        self.pai3 = ""
        self.pai4 = ""
        self.xifapai()

    def xifapai(self):  # 洗牌发牌，发请0位置抢地主，积分为0
        l0 = ["0" + str(x) for x in range(5, 10)]
        l1 = [str(x) for x in range(10, 15)] + l0
        l2 = ["ht", "fk", "ho", "mh"]
        lzong = [x + y for x in l2 for y in l1]
        random.shuffle(lzong)
        print(lzong)
        s1 = "^".join(lzong[:10])
        self.pai1 = s1
        s2 = "^".join(lzong[10:20])
        self.pai2 = s2
        s3 = "^".join(lzong[20:30])
        self.pai3 = s3
        s4 = "^".join(lzong[30:])
        self.pai4 = s4

        c.send((sf + self.name + "^" + self.wei1 + "^" + s1 + "信息间隔").encode())
        print(sf + self.name + "^" + self.wei1 + "^" + s1 + "信息间隔")
        c.send((sf + self.name + "^" + self.wei2 + "^" + s2 + "信息间隔").encode())
        print(sf + self.name + "^" + self.wei2 + "^" + s2 + "信息间隔")
        c.send((sf + self.name + "^" + self.wei3 + "^" + s3 + "信息间隔").encode())
        print(sf + self.name + "^" + self.wei3 + "^" + s3 + "信息间隔")
        c.send((sf + self.name + "^" + self.wei4 + "^" + s4 + "信息间隔").encode())
        if "ht05" in lzong[:10]:
            c.send((sf+self.name+"^"+self.wei1+"^随便出牌"+"信息间隔").encode())
        elif "ht05" in lzong[10:20]:
            c.send((sf+self.name+"^"+self.wei2+"^随便出牌"+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei2, self.wei3, self.wei4, self.wei1
        elif "ht05" in lzong[20:30]:
            c.send((sf+self.name+"^"+self.wei3+"^随便出牌"+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei3, self.wei4, self.wei1, self.wei2
        elif "ht05" in lzong[30:]:
            c.send((sf+self.name+"^"+self.wei4+"^随便出牌"+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei4, self.wei1, self.wei2, self.wei3

    # def fadizhupai(self):  # 发给三家地主牌是什么
    #     #     connfd2.send(("地主名^"+name+"^"+str(n)+"^" + s4+"^下家").encode())

    #     c.send((sf + self.name + "^" + self.wei1 + "^地主名^" + self.dizhuming +
    #             "^" + str(self.fen) + "^" + self.gong + "^本人" + "信息间隔").encode())

    #     c.send((sf+self.name+"^"+self.wei2+"^地主名^"+self.dizhuming +
    #             "^"+str(self.fen)+"^" + self.gong+"^上家"+"信息间隔").encode())

    #     c.send((sf+self.name+"^"+self.wei3+"^地主名^"+self.dizhuming +
    #             "^"+str(self.fen)+"^" + self.gong+"^下家"+"信息间隔").encode())

    #     c.send((sf+self.name+"^"+self.wei1+"^" +
    #             self.pai1+"^"+self.gong+"信息间隔").encode())
    #     self.fasuibchu()

    def fasuibchu(self):  # 发送随便出牌
        c.send((sf+self.name+"^"+self.wei1+"^随便出牌"+"信息间隔").encode())

    def fayaodachu1(self):  # 发送要大出牌
        c.send((sf+self.name+"^"+self.wei2+"^位置二要大出牌"+"信息间隔").encode())

    def fayaodachu2(self):  # 发送当已经有一个人过后打，要大出牌
        c.send((sf+self.name+"^"+self.wei3+"^位置三要大出牌"+"信息间隔").encode())

    def fayaodachu3(self):  # 发送当已经有一个人过后打，要大出牌
        c.send((sf+self.name+"^"+self.wei4+"^位置四要大出牌"+"信息间隔").encode())

    def weizhichu1(self, lx):  # 发送位置0出牌打牌，给其他人
        c.send((sf+self.name+"^"+self.wei2+"^上家出牌^"+"^".join(lx)+"信息间隔").encode())
        c.send((sf+self.name+"^"+self.wei3+"^对家出牌^"+"^".join(lx)+"信息间隔").encode())
        c.send((sf+self.name+"^"+self.wei4+"^下家出牌^"+"^".join(lx)+"信息间隔").encode())
        if lx[-1] != "0":
            self.fayaodachu1()

    def weizhichu2(self, lx):  # 发送位置１出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei3+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei4+"^对家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1+"^下家过"+"信息间隔").encode())
            self.fayaodachu2()
        else:
            c.send((sf+self.name+"^"+self.wei3 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei4 +
                    "^对家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei2, self.wei3, self.wei4, self.wei1
            if lx[-1] != "0":
                self.fayaodachu1()

    def weizhichu3(self, lx):  # 发送位置２出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei4+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1+"^对家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2+"^下家过"+"信息间隔").encode())
            self.fayaodachu3()
        else:

            c.send((sf+self.name+"^"+self.wei4 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei1 +
                    "^対家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei3, self.wei4, self.wei1, self.wei2
            if lx[-1] != "0":
                self.fayaodachu1()

    def weizhichu4(self, lx):  # 发送位置3出牌打牌，给其他人
        if lx[0] == "过":
            c.send((sf+self.name+"^"+self.wei1+"^上家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2+"^对家过"+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei3+"^下家过"+"信息间隔").encode())
            self.fasuibchu()
        else:

            c.send((sf+self.name+"^"+self.wei1 +
                    "^上家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei2 +
                    "^対家出牌^"+"^".join(lx)+"信息间隔").encode())
            c.send((sf+self.name+"^"+self.wei3 +
                    "^下家出牌^"+"^".join(lx)+"信息间隔").encode())
            self.wei1, self.wei2, self.wei3, self.wei4 = self.wei4, self.wei1, self.wei2, self.wei3
            if lx[-1] != "0":
                self.fayaodachu1()


def chuli(s, fj):

    if fj[2] == "位置一出牌":  # 位置一出牌，出的打牌
        s.weizhichu1(fj[3:])
    elif fj[2] == "位置二出牌":  # 位置二出牌，出的打牌
        s.weizhichu2(fj[3:])
    elif fj[2] == "位置三出牌":  # 位出牌，出的打牌
        s.weizhichu3(fj[3:])
    elif fj[2] == "位置四出牌":  # 位出牌，出的打牌
        s.weizhichu4(fj[3:])
    return s


pool = Pool(processes=10)


while True:
    f = c.recv(1024)
    fj = f.decode()
    if fj == "":
        break
    fj = fj.split("^")
    print(fj)
    if fj[0] == "开房间吧":
        a = Fangjian(fj[1])
        d[fj[1]] = a
    if fj[0] == "出牌":  # 出牌　房间号
        s = d[fj[1]]
        d[fj[1]] = pool.apply(chuli, (s, fj))
