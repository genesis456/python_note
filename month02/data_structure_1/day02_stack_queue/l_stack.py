"""
l_stack.py
 栈的链式模型
重点代码

思路:
1.通过节点存储数据达到链式存储的目的
2. 封装方法,实现栈的基本操作(入栈,出栈,栈空,查看栈顶）
3.top为栈顶，在链表的头作为栈顶位置（不需要每次遍历）
"""

#自定义异常
class StackError(Exception): #一般情况都是继承Exception类的
    pass

#节点类
class Node:

    def __init__(self,val,next = None):
        """
              val: 有用数据
              next: 下一个节点引用
        """

        self.val = val  # 有用数据
        self.next = next #循环下一个节点关系

#链式栈模型
class LStack:
    # top作为栈顶的标记
    def __init__(self):
        self.__top = None

    # 入栈
    def push(self,val):
      self.__top = Node(val,self.__top)
      # node = Node(val)  创建一个初始节点
      # node.next = self.__top　　将节点绑定为栈顶
      # self.__top = node　　将栈顶移动到下一节点上

    #空栈
    def is_empty(self):
        return self.__top is None

    #出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        else:
            data = self.__top.val
            self.__top = self.__top.next #移动节点（将栈顶移到下一节点上）
            return data

    #查看栈顶
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__top.val


if __name__ == "__main__":
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(3)
    print(ls.pop())
    print(ls.top())

