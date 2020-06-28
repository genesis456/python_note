"""
    练习：定义对象计数器。
    定义老婆类，创建３个老婆对象。
    可以通过类变量记录老婆对象个数，
    可以通过类方法打印老婆对象个数。
    要求：画出内存图.
"""

# class Wife():
#     count = 0
#     def __init__(self,name,sex):
#
#         self.name = name
#         self.sex = sex
#         Wife.count += 1
# wife01 =  Wife("carry","女")
# wife02 =  Wife("kill","女")
# wife03 =  Wife("李梅","女")
# print(Wife.count)
# ##这个是直接访问类变量

class Wife():
    count = 0

    @classmethod  #类定义
    def print_count(cls):#类方法名称，用来操作类变量
        print("我有%d房"%cls.count)

    def __init__(self,name,sex):

        self.name = name
        self.sex = sex
        Wife.count += 1
wife01 =  Wife("carry","女")
wife02 =  Wife("kill","女")
wife03 =  Wife("李梅","女")
Wife.print_count()
