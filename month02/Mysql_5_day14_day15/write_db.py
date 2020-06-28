"""
write_db.py
pymysql写操作示例（insert update delete)
"""

import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

#获取游标
cur = db.cursor()

#写数据库
try:
    #写sql语句执行
    #插入操作
    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score:")

    #将变量插入sql语句合成最终操作语句
    # #根据表结构可知，name是一定要加引号的
    # sql = "insert into class (name,age,score) values ('%s',%s,%s);"%(name,age,score)
    #
    # cur.execute(sql)  #执行

    #有比以上更方便的办法
    # sql = "insert into class (name,age,score) values (%s,%s,%s);"
    # cur.execute(sql,[name,age,score])  # 会先将后面列表中的参数按表结构的标准传入values后面的语句中，并执行sql语句

    #修改操作
    # sql = "update interest set price=11800 where name='李聪';"
    # cur.execute(sql)

    #删除操作
    sql = "delete from class where age=15 limit 1;"  #删除年龄为15的，只限1个
    cur.execute(sql)


    db.commit()  #写操作一定要提交



except Exception as e:
    db.rollback()  #退回到commit执行之前的数据库状态
    print(e)



#关闭游标和数据库
cur.close()
db.close()
