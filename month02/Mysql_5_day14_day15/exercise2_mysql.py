"""
练习2：
1.编写一个而程序模拟注册和登录的过程
    *创建一个user表包含用户名和密码字段
    *应用程序中模拟注册和登录功能
        注册则输入用户名密码将用户名密码存入到数据库
        (用户名不能重复)

        登录则进行数据库比对，如果有该用户则打印登录成功
        否则让重新输入
"""
import pymysql



# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标（操作数据库，执行sql语句的）
cur = db.cursor()

#注册
def register():
    name = input("用户名：")
    code = input("密码：")
    #判断用户名是否重复
    sql = "select * from user where user_name='%s'"%name  #若不存在返回一个空
    cur.execute(sql)  #执行sql语句
    result = cur.fetchone()   #取出存在的一个，若不存在返回一个空
    if result:
        return False  #存在返回false
    try:
        sql = "insert into user (user_name,code) values (%s,%s);"
        cur.execute(sql,[name,code])
        db.commit()
        return True
    except:
        db.rollback()
        return False

#登录
def login():
    name = input("用户名：")
    code = input("密码：")
    sql = "select * from user where user_name='%s' and code='%s'"%(name,code)
    cur.execute(sql)
    result = cur.fetchone()  # 取出存在的一个，若不存在返回一个空
    if result:
        return True



while True:
    print("""             ============
             1.注册　2.登录 
             ============""")
    cmd = input("输入命令：")
    if cmd == '1':
        #执行注册
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        #执行登录
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")
    else:
        print("暂无该服务")


# 关闭游标和数据库
cur.close()
db.close()







