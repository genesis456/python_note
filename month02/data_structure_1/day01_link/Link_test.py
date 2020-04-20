from linklist import *
import time
l = [1,2,8,6]
# l = []
# for i in range(999999):
#     l.append(i)

link = LinkList()
link.init_list(l)

tm = time.time()
#列表遍历
# for i in l:
#     print(i)
#链表遍历
# link.show()
# print("time:",time.time()-tm)

# l.insert(0,8866)
# link.head_insert(8866)  #头插
# link.insert(-100,88665)  #  如果插入超前（只会插入在头部，效率会高一点），
# 如果插入索引超后（会插入在尾部，效率就会低）
# link.delete(2)
link.show()
print(link.get_index(3))  #获取索引３的值
print("time00:",time.time()-tm)
##该实验得出列表遍历比链表遍历速度更快
"""
测算一个大列表，插入一个数据的时间
"""

# import time
# from linklist import *
#
#
#
# # link.init_list(l)
#
# tm = time.time()

# print(time.time() - tm)