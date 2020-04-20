"""
mysql.py
pymysql  操作数据库基本流程演示
"""


import pymysql

#连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')


#获取游标（操作数据库，执行sql语句的）
cur = db.cursor()

#执行sql语句
sql = "insert into class values (7,'索隆',20,'m',99,'2020-1-16');"

cur.execute(sql)  #执行语句

db.commit()  #将写操作提交（读操作不需要），多次写操作一同提交

#关闭游标和数据库
cur.close()
db.close()








