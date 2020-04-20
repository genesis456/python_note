import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='games',
                     charset='utf8')

cur = db.cursor()

def forget():
    while True:
        name = input("请输入英雄：")
        if not name:
            break
        occupation = input("职业：")
        price = input("  价格：")

        try:
            sql = 'insert into glory_king (name,occupation,price) values (%s,%s,%s);'

            cur.execute(sql,[name,occupation,price])

            db.commit()
        except Exception as e:
            db.rollback()
            print(e)

    cur.close()
    db.close()
forget()