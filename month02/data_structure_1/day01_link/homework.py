"""
作业 : 1. 将重点代码能够看懂,独立完成
      2. 给出两个有序的链表L1,L2 .
         在不创建新的链表的基础上将两个链表合并为一个
         要求合并后的链表仍为有序

"""

from linklist import *

# 创建两个链表,初始化数值
L1 = LinkList()
L2 = LinkList()
L1.init_list([1,5,9,13,16])
L2.init_list([3,4,8,15])
L1.show()
print("--------")
L2.show()
print("--------")


def orderly_merge(l1,l2):
    """
    将两个链表有序合并
    """
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val :  #比较的是next中的值
            p = p.next   #向后移，传递下一节点
        else:
            tmp = p.next  #如果那个点的值较大，先做标记
            p.next = q   #将Ｐ的位置移到q上
            q = tmp  #将较大值赋给新的q上
            p = p.next   #继续向后移动，重复执行
    p.next = q  #到末尾两个比较时，直接将Ｑ值给p.next

orderly_merge(L1,L2)
L1.show()

#切记画图理解，看笔记

