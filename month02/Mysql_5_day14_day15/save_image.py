"""
save_image.py
二进制文件演示
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

#存储图片
# with open('timg.jpeg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image=%s where name='索隆';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

#从数据库提取图片
sql = "select image from class where name='索隆';"
cur.execute(sql)
data = cur.fetchone()  #获取查询结果集的第一条数据，查找到返回一个元组
with open('emin.jpg','wb') as f:
    f.write(data[0])


#关闭游标和数据库
cur.close()
db.close()