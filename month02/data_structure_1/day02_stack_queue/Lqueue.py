"""
lqueue.py  链式队列
重点代码

思路:1.基于链表构建队列模型
2.链表的开端作为队头，结尾作为队尾
3.队头队尾分别添加标记，避免每次插入数据都遍历链表（为什么要每次遍历）
4. 队头和队尾重叠时认为队列为空
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

#链式队列操作
class LQueue:
    def __init__(self):
        # 定义队头,队尾

        self.front = self.rear = Node(None)

    # 判断队列为空
    def is_empty(self):
        return self.front == self.rear

    # 入队  rear动
    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    # 出队　front动
    def dequeue(self):
        if self.front == self.rear:
            raise StackError("Queue is empty")

        # front移动到的节点已经出队
        self.front = self.front.next  #front移动到的下一个节点
        return self.front.val

if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(30)
    lq.enqueue(50)
    while not lq.is_empty():
        print(lq.dequeue())

