#! /usr/bin/python3
from pymysql import *

class Mydatabase:
    def __init__(self,host='localhost',port=3306,db='gamehall',
                 user='root',passwd='123456',charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,port=
               self.port,db=self.db,user=self.user,
               passwd=self.passwd,
               charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def check_usrexist(self,name): #注册时判断用户名存在性
        self.open()
        sql = "select * from user where username='%s'"
        self.cursor.execute(sql %name)
        r = len(self.cursor.fetchall())
        self.conn.commit()
        self.close()
        if r > 0:
            return 0
        else:
            return 1

    def check_login(self,name,passwd): #判断用户名密码的一致性

        if self.check_usrexist(name):
            return 0
        self.open()
        sql = "select password from user where username='%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        if r[0] == passwd:
            return 1
        else:
            return 0

    def insert_user(self,name,passwd,niname,telnum): #新用户注册
        self.open()
        sql = "insert into user(username,password,user_nicheng,telnum)\
               values('%s',%d,'%s','%s')"
        self.cursor.execute(sql %(name,int(passwd),niname,telnum))
        self.conn.commit()

        sql = "select userid from user where username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()

        sql = "insert into game(uid) values(%d)"
        r = self.cursor.execute(sql %r[0])
        self.conn.commit()

        self.close()

    def user_login(self,name):  #用户每次登录 登录次数加一
        self.open()
        sql = "update user set login_count = login_count + 1\
               where username = '%s'"
        self.cursor.execute(sql %name)
        self.conn.commit()
        self.close()

    def check_loign_count(self,name): #获取用户的登录次数
        self.open()
        sql = "select login_count from user where username='%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r[0]

    def check_phonenum(self,name): #手机号验证
        self.open()
        sql = "select telnum from user where username='%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r[0]

    def update_paswd(self,name,number): #修改密码
        self.open()
        sql = "update user set telnum = %d where username = '%s'"
        self.cursor.execute(sql %(name,number))
        self.conn.commit()
        self.close()

    def check_vitality(self,name):  #查看用户的活跃度
        self.open()
        sql = "select game.vitality from game inner join user \
               on user.userid = game.uid where user.username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r[0]

    def check_gold(self,name):  #查看用户的金币
        self.open()
        sql = "select game.gold from game inner join user \
               on user.userid = game.uid where user.username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r[0]

    def count_changci(self,name):  #查看用户的总场数，胜场数，负场数
        self.open()
        sql = "select game.total_count,game.win_count,game.lose_count\
               from game inner join user on user.userid = \
               game.uid where user.username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r

    def check_integr_level(self,name):  #查看用户的积分,段位
        self.open()
        sql = "select game.integration,game.level_flag\
               from game inner join user on user.userid = \
               game.uid where user.username = '%s'"
        self.cursor.execute(sql %name)
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r

    def login_gifts(self,name,v):   #根据登录次数获赠活跃度
        self.open()
        sql = "update user inner join game on user.userid \
               = game.uid set game.vitality = game.vitality + %d\
               where user.username = '%s'"
        self.cursor.execute(sql %(v,name))
        self.conn.commit()
        self.close()

    def win_update(self,name,w_gold,w_integration): #赢比赛，修改相应的表中数值
        self.open()
        sql = "update user inner join game on user.userid \
               = game.uid set game.gold = game.gold + %d,\
               game.integration = game.integration + %d,\
               game.total_count = game.total_count + 1,\
               game.win_count = game.win_count + 1\
               where user.username = '%s'"
        self.cursor.execute(sql %(name,w_gold,w_integration))
        self.conn.commit()
        self.close()

    def lose_update(self,name,l_gold,l_integration): #输比赛，修改相应的表中数值
        self.open()
        sql = "update user inner join game on user.userid \
               = game.uid set game.gold = game.gold - %d,\
               game.integration = game.integration - %d,\
               game.total_count = game.total_count + 1,\
               game.lose_count = game.lose_count + 1\
               where user.username = '%s'"
        self.cursor.execute(sql %(name,w_gold,w_integration))
        self.conn.commit()
        self.close()

    def win_gifts(self,): #赢得游戏 获得礼物
        self.open() 
        sql = "update user inner join game on user.userid \
               = game.uid set game.vitality = game.vitality + %d\
               where user.username = '%s'"
        self.cursor.execute(sql %(v,name))
        self.conn.commit()
        self.close()

    def levelup(self): #段位提升获得礼物
        self.open() 
        sql = "update user inner join game on user.userid \
               = game.uid set game.vitality = game.vitality + %d\
               where user.username = '%s'"
        self.cursor.execute(sql %(v,name))
        self.conn.commit()
        self.close()

    def shop(self): #购物后修改相关数值
        self.open() 
        sql = "update user inner join game on user.userid \
               = game.uid set game.vitality = game.vitality + %d\
               where user.username = '%s'"
        self.cursor.execute(sql %(v,name))
        self.conn.commit()
        self.close()
    
    def save_levelflag(self,name,l):  #保存段位标记
        self.open()
        sql = "update user inner join game on user.userid \
               = game.uid set game.level_flag = %d\
               where user.username = '%s'"
        self.cursor.execute(sql %(l,name))
        self.conn.commit()
        self.close()

    def check_level(self,name): #查看对应段位
        self.open()
        sql = "select level.level_name \
               from game inner join level \
               on game.level_flag = level.level_id\
               inner join user on user.userid = game.uid\
               where user.username = '%s'"
        self.cursor.execute(sql %(name))
        r = self.cursor.fetchone()
        self.conn.commit()
        self.close()
        return r[0]


# mdb = Mydatabase()

# mdb.insert_user('周勇',77777,'dda','13684934874')
# uname = input("请输入你的姓名：")
# passwd = input("请输入你的密码:")
# # mdb.check_usrexist(uname)
# mdb.check_login(uname,passwd)
# mdb.login_gifts("段然",1000)
# r = mdb.check(uname)
# print(r)
# mdb.user_login("段然")
# mdb.user_login("王鹏")
# mdb.user_login("周勇")
# mdb.save_levelflag("段然",3)
# r = mdb.check_level("段然")
# print(r)