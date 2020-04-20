"""
日期：19/12/2019
作者：周乐
装饰器练习：
    在不改变原有功能（存取钱）的定义与调用情况下，
    　　增加验证帐号的功能
"""

def verify_permissions(func):  #采用了闭包
    def wrapper(*args,**kwargs):
        print("验证帐号")
        func(*args,**kwargs)
    return wrapper

@verify_permissions   #拦截
def deposit(money):
    print("存%d钱咯" %money)
@verify_permissions
def withdraw(login_id,pwd):
    print("取钱咯",login_id,pwd)

deposit(10000)
withdraw("zs",123)














