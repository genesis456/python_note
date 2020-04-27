"""
linklist.py
功能：实现单链表的构建和功能操作
重点代码
"""

#创建节点类
class Node:
    """
    思路：自定义类视为节点类，类中的属性为数据内容
        　　写一个next属性，用来和下一个节点建立关系
    """
    def __init__(self,val,next=None):
        """
              val: 有用数据
              next: 下一个节点引用
        """

        self.val = val  # 有用数据
        self.next = next #循环下一个节点关系

#做链表的操作
class LinkList:
    """
    思路：　生成单链表，通过实例化的对象就代表一个链表
        　　可以调用具体的操作方法完成各种功能
    """
    def __init__(self): #链表的初始化节点，没有有用数据，但是便于标记链表的开端
        self.head = Node(None) #初始化链表，添加一组节点

    #通过list_为链表添加一组节点
    def init_list(self,list_):
        p = self.head  #P作为移动变量
        for i in list_: #遍历到一个值就创建一个节点
            p.next = Node(i)  #将第二个节点绑定到第一个节点的next上
            p = p.next  #将第二个节点的next交付给Ｐ，以此遍历

    #遍历链表
    def show(self):
        p = self.head.next  #P代表第一个有值的节点
        while p is not None:  #判断对象是否相等（is或is not）,判断值是否相等（＝＝或！＝）
            print(p.val)
            p = p.next  #P向后移动
        """
        总结：链表的创建（首先创建一个模型类：节点数据和绑定下一节点关系的next－－－＞
        创建一个功能控制类：建立第一个节点，然后将第一个节点的next关系绑定在第二个节点上）
        """
    #判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False
    #清空链表
    def clear(self):
        self.head.next = None
    #尾部插入
    def append(self,val):
        p = self.head #P移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val)#最后添加节点
    #头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
    #指定位置插入
    def insert(self,index,val):
        p = self.head
        for item in range(index):
            #超出位置最大范围结束循环
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node
    #删除节点
    def delete(self,x):
        p = self.head
        #结束循环必然两个条件其一为假
        while p.next and p.next.val != x:  #p.next相当于p.next is not None(前者为假，后续就不再判断）
            p = p.next

        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next
    #获取某个节点值，传入节点位置获取节点值
    def get_index(self,index):
        if index <0:
            raise IndexError("index out of range")

        #循环移动p
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")

            p = p.next
        return p.val

# l = LinkList()
# l.init_list([2,5,3,8,9])
# l.show()

