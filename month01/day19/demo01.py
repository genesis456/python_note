"""
   装饰器
"""
#需求：对以下两个功能增加权限验证．
"""
#需要增加的功能
def verify_permissions():
    print("权限验证")

#已有功能
def enter_background():
    verify_permissions()
    print("进入后台")

def delete_order():
    verify_permissions()
    print("删除订单")

enter_background()
delete_order()
#缺点：增加新功能，需要修改已有功能．［］
"""
"""
#需要增加的功能
def verify_permissions(func):  #采用了闭包
    def wrapper():
        print("权限验证")
        func()
    return wrapper

#已有功能
def enter_background():
    print("进入后台")

def delete_order():
    print("删除订单")

#enter_background = 新功能　＋　旧功能
enter_background = verify_permissions(enter_background) #拦截已有功能
delete_order = verify_permissions(delete_order)

enter_background()
delete_order()
缺点：每次拦截对已有功能（enter_background)的调用，不科学
"""
"""
#需要增加的功能
def verify_permissions(func):  #采用了闭包
    def wrapper():
        print("权限验证")
        func()
    return wrapper

#已有功能
#enter_background = verify_permissions(enter_background)
@verify_permissions
def enter_background():
    print("进入后台")
@verify_permissions
def delete_order():
    print("删除订单")

enter_background()
delete_order()
缺点：如果已有功能参数不统一，则无法包装
"""
#需要增加的功能
def verify_permissions(func):  #采用了闭包
    def wrapper(*args,**kwargs):   #*args是传入的参数可以无限，**kwargs合并字典
        print("权限验证")
        func(*args,**kwargs)
    return wrapper

#已有功能
@verify_permissions
def enter_background(login_id,pwd):
    print(login_id,pwd,"进入后台")
@verify_permissions
def delete_order(id):
    print("删除订单",id)

enter_background(102,00)
delete_order(10001)
















