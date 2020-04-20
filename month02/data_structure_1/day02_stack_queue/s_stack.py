"""
s_stack.py
 栈模型的顺序存
重点代码

思路 ：１.顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
    ２.将列表功能封装,实现顺序栈的类,只提供栈的操作功能

功能: 出栈, 入栈,判断栈空,查看栈顶元素
"""

#自定义异常
class StackError(Exception): #一般情况都是继承Exception类的
    pass


#顺序栈
class SStack:
    def __init__(self):
        #空列表就是栈的存储空间
        #列表的最后一个元素作为栈顶元素
        self._elems = []

    # 单下划线是伪私有变量（约定俗成的，可以外部访问，表示不希望这个变量在外部被直接调用 ）

    # 入栈
    def push(self,val):
        self._elems.append(val)
    # 判断空栈
    def is_empty(self):
        """
        判断空栈，若是空，返回Ｔrue,否则Ｆalse
        :return: 布尔值
        """
        return self._elems == []

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")  #表示该列表是空栈
        return self._elems.pop()   #pop() 函数用于移除列表中的一个元素（默认最后一个元素）

    # 查看栈顶
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")  #表示该列表是空栈
        return self._elems[-1]  #进来的最后一个是栈顶(也就是栈的末尾元素)


if __name__ == "__main__":
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(40)
    while not st.is_empty():
        print(st.pop())
