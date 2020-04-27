"""
squeue.py
队列的顺序存储
思路 :
1. 基于列表完成数据存储
2. 对列表功能进行封装
3.列表的头部作为队头，尾部作为队尾功能：入队(enqueue),出队(dequeue),判断队列为空
队列的原则：
队尾进队头出（先进先出）
"""

#自定义异常
class QueueError(Exception):
    pass

class SQueue:
    #设置空列表作为队列存储空间
    def __init__(self):
        self._elems = [] #队头   #单下划线是伪私有变量（约定俗成的，可以外部访问，表示不希望这个变量在外部被直接调用 ）

    #判断队列为空
    def is_empty(self):
        return self._elems == []

    #入队  列表尾部定义为队尾
    def enqueue(self,val):
        self._elems.append(val)

    #出队　　列表的第一个元素
    def dequeue(self):
        if self.is_empty():
            raise QueueError("pop from empty SQueue")
        else:
            return self._elems.pop(0)  #队头出
            #pop() 函数用于移除列表中的一个元素（默认最后一个元素）

if __name__ == "__main__":
    sq = SQueue()

    for i in range(10):

        sq.enqueue(i)
    # while not sq.is_empty():
    #     print(sq.dequeue())

#########将队列进行翻转###############

    from s_stack import *
    st = SStack()
    #循环出队入栈
    while not sq.is_empty():    #当队不为空时，出队往栈里入
        st.push(sq.dequeue())
    #循环出栈入队
    while not st.is_empty():    #当栈不为空时，出栈往队里入
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())
