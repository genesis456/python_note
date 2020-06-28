import getpass   #隐藏输入
import hashlib   #转换加密的


#可以隐藏输入的内容，可以用作密码的隐藏保护
pwd = getpass.getpass("pw:")  #相当Input（）
print(pwd)

# hash对象
hash = hashlib. md5() #生成对象,md5加密

#算法加盐(#$awv3_ (盐))　　将盐和原密码混合
#   abc123#$awv3_

# hash = hashlib.md5 ("*#06L ".encode() ) #*#06L作为盐，进行加密

hash. update(pwd.encode())#算法加密
pwd = hash. hexdigest() #提取加密后的密码，
print(pwd)
#
#
#

# """
# ｄｉｃｔ 所有数据库交互
# 提供数据库连接，以及功能交互
# """
# import pymysql
# import hashlib
#
# salt = b"*#06#"  # 加密专用盐
#
#
# # 　加密处理函数
# def encryption(passwd):
#     # 对密码进行加密处理
#     hash = hashlib.md5(salt)
#     hash.update(passwd.encode())
#     return hash.hexdigest()  # 获取存储密码
#
#
# class Database:
#     def __init__(self):
#         # 连接数据库
#         self.db = pymysql.connect(host='localhost',
#                                   port=3306,
#                                   user='root',
#                                   password='123456',
#                                   database='dict',
#                                   charset='utf8')
#
#         # 创建游标 (操作数据库语句,获取查询结果)
#         self.cur = self.db.cursor()
#
#     def close(self):
#         # 关闭游标和数据库
#         self.cur.close()
#         self.db.close()
#
#     def register(self, name, passwd):
#         # 判断用户名
#         sql = "select * from user where name='%s'" % name
#         self.cur.execute(sql)
#         resule = self.cur.fetchone()
#         if resule:
#             return False
#
#         # 　加密
#         passwd = encryption(passwd)
#
#         # 插入用户
#         try:
#             sql = "insert into user (name,passwd) values (%s,%s)"
#             self.cur.execute(sql, [name, passwd])
#             self.db.commit()
#             return True
#         except:
#             self.db.rollback()
#             return False
#
#     def login(self, name, passwd):
#         passwd = encryption(passwd)  # 加密转换
#
#         sql = "select * from user where name='%s' and passwd='%s'" % (name, passwd)
#         self.cur.execute(sql)
#         result = self.cur.fetchone()
#         if result:
#             return True
#         else:
#             return False
#
#     def query(self, word):
#         sql = "select mean from words where word='%s'" % word
#         self.cur.execute(sql)
#         r = self.cur.fetchone()
#         if r:
#             return r[0]
#
#     # 　插入记录
#     def insert_history(self, name, word):
#         sql = "insert into hist (name,word) \
#         values (%s,%s)"
#         try:
#             self.cur.execute(sql, [name, word])
#             self.db.commit()
#         except:
#             self.db.rollback()
#
#     def history(self,name):
#         sql = "select name,word,time from hist \
#         where name='%s' order by time desc " \
#               "limit 10"%name
#         self.cur.execute(sql)
#         return self.cur.fetchall()
#
#
#
#
#
#
#
# """
# dict 服务端
# 功能: 业务逻辑处理
# 模型: Process 多进程 tcp 并发
# """
#
# from socket import *
# from multiprocessing import Process
# import os,signal
# from dict_db import Database
# from time import sleep
#
# HOST = '0.0.0.0'
# PORT = 8888
# ADDR = (HOST,PORT)
#
# #　数据库操作对象
# db = Database()
#
# #　处理注册
# def do_register(c,data):
#     tmp = data.split(' ')
#     name = tmp[1]
#     passwd = tmp[2]
#     if db.register(name,passwd):
#         c.send(b'OK')
#     else:
#         c.send(b'Fail')
#
# #　处理登录
# def do_login(c,data):
#     tmp = data.split(' ')
#     name = tmp[1]
#     passwd = tmp[2]
#     if db.login(name,passwd):
#         c.send(b'OK')
#     else:
#         c.send(b'Fail')
#
# #　查询单词
# def do_query(c,data):
#     tmp = data.split(' ')
#     name = tmp[1]
#     word = tmp[2]
#
#     #　插入历史记录
#     db.insert_history(name,word)
#
#     #　通过数据库找到单词 (找到返回解释，找不到None)
#     mean = db.query(word)
#     if mean:
#         msg = "%s : %s"%(word,mean)
#     else:
#         msg = "没有找到该单词"
#     c.send(msg.encode())
#
# #　历史记录
# def do_hist(c,data):
#     name = data.split(' ')[1]
#     r = db.history(name)
#     for i in r:
#         #　ｉ -->(name  word  time)
#         msg = "%s　%-16s  %s"%i
#         sleep(0.1)
#         c.send(msg.encode())
#     sleep(0.1)
#     c.send(b"##")
#
# # 客户端处理函数,循环收发消息
# def handle(c):
#     while True:
#         data = c.recv(1024).decode()
#         if not data or data[0] == 'E':
#             os._exit(0)
#         elif data[0] == 'R':
#             do_register(c,data)
#         elif data[0] == 'L':
#             do_login(c,data)
#         elif data[0] == 'Q':
#             do_query(c,data)
#         elif data[0] == 'H':
#             do_hist(c, data)
#
#
# # 程序的启动入口
# def main():
#     # 创建监听套接字
#     s = socket()
#     s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     s.bind(ADDR)
#     s.listen(5)
#
#     signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#     print("Listen the port 8888....")
#
#     while True:
#         # 循环等待客户端连接
#         try:
#             c,addr = s.accept()
#             print("Connect from",addr)
#         except KeyboardInterrupt:
#             db.close() #　关闭数据库连接
#             os._exit(0)
#         except Exception as e:
#             print(e)
#             continue
#
#         # 创建新的进程处理请求
#         client = Process(target=handle,args=(c,))
#         client.daemon = True
#         client.start()
#
# if __name__ == '__main__':
#     main()
#
#
#
