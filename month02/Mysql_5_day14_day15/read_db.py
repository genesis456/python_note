"""
read_db.py
pymysql  读操作示例（selet)
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

#获取数据库数据
sql = "select * from class where sex='m';"

cur.execute(sql)   #执行语句,执行正确后cur调用函数获取结果

# #获取一个查询结果(只拿其中一个）
# one_row = cur.fetchone()    #返回的是个元组
# print(one_row)
#
# #获取多个查询结果
# many_row = cur.fetchmany(2)  #查询2个,从上次拿出的地方继续往后拿
# print(many_row)

#获取所有查询结果
all_row = cur.fetchall()
print(all_row)



#关闭游标和数据库
cur.close()
db.close()



