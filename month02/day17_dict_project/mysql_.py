"""
数据库操作模块
思路：
将数据库操作封装一个类，将dict_server需要的数据库操作
功能分别写成方法，在dict_server中实例化对象，需要什么方法可以直接
调用
"""

import pymysql
import hashlib

salt = b"*#06#"  # 加密专用盐

class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             passwd='123456',
                             database='dict',
                             charset='utf8')
        # 创建游标 (操作数据库语句,获取查询结果)
        self.cur = self.db.cursor()


    #断开数据库连接
    def close(self):
        self.cur.close()
        self.db.close()


    #注册操作
    def register(self, name, passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()  #存在返回元祖，否则返回None
        #查找到则用户存在
        if r:
            return False

        #密码加密存储处理
        passwd = self.hash_passwd(passwd)

        #插入数据库
        try:
            sql = "insert into user (name,passwd) values (%s,%s)"
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except :
            self.db.rollback()
            return False

    #密码加密
    def hash_passwd(self, passwd):
        hash = hashlib.md5(salt)  # 用户名与盐再合成新盐进行加密（更难以破解）
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 加密后的密码
        return passwd

    #登录处理
    def login(self,name,passwd):
        # 先进行密码加密
        passwd = self.hash_passwd(passwd)

        #数据库查找
        sql = "select * from user where name='%s' and passwd='%s'" % (name,passwd)

        self.cur.execute(sql)
        r = self.cur.fetchone()
        # 若查找到有该数据则允许登录
        if r:
            return True
        else:
            return False

    #查单词
    def query(self,word):
        sql = "select mean from words where word='%s';" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        #如果找到r－－＞(mean),否则默认返回None
        if r:
            return r[0]

    #插入历史记录
    def insert_hist(self,name,word):
        sql = "insert into hist (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    #查询历史记录
    def get_hist(self,name):
        sql = "select name,word,time from hist where name = '%s' " \
              "order by time desc limit 10" % name
        self.cur.execute(sql)
        return self.cur.fetchall()


