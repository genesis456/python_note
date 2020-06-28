"""
练习：将单词本存入数据库

1.创建数据库　dict  (utf8)
2.创建数据表　words　　将单词和单词解释分别存入不同的字段中
3.将单词存入words单词表　　超过19500即可
"""
import pymysql
import re


db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

#获取游标
cur = db.cursor()

#将单词本写入数据库

f = open('English_dict')

# for line in f:
#     los = line.split(" ")
#     text = ' '.join(los[1:]).strip()
#     try:
#         sql = "insert into words (word,explains) values (%s,%s);"
#         cur.execute(sql,[los[0],text])
#         db.commit()  #提交数据
#
#     except Exception as e:
#         db.rollback()  #退回到commit执行之前的数据库状态
#         print(e)

#用正则表达式比上面简便
sql = "insert into words (word,explains) values (%s,%s);"

for line in f:
    #获取单词和解释
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]   #要将元祖拿出来
    # 如果正则表达式有子组则只能获取到子组对应的内容,返回的结果是一个列表套元祖［（子组1，子组2）］
    try:
        cur.execute(sql,tup)
        db.commit()
    except:
        db.rollback()


f.close()
cur.close()
db.close()