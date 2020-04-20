"""
逆波兰表达式
"""
from s_stack import *

# st = SStack()
# while True:
#     exp = input()
#     tmp = exp.split(" ") #按空格分割
#     for i in tmp:
#         if i not in ["+","-","*","/","p"]:
#             st.push(float(i))  #如果是数字就添加进栈中
#         elif i == "+":
#             x = st.pop()
#             y = st.pop()
#             st.push(y+x)   #先出来的
#         elif i == "-":
#             x = st.pop()
#             y = st.pop()
#             st.push(y-x)
#         elif i == "*":
#             x = st.pop()
#             y = st.pop()
#             st.push(y*x)
#         elif i == "/":
#             x = st.pop()
#             y = st.pop()
#             st.push(y/x)
#         elif i == "p":
#             print(st.top())

#经自己优化后
cs = SStack()
def dcmess():
    while True:
        rt = input("请输入表达式(q键退出，c键清空栈元素)：")
        if rt == "q":
            break
        if rt == "c":
            while not cs.is_empty():
                cs.pop()
            continue
        st = rt.split(" ")
        for i in st:
            if i not in ("+","-","*","/","p"):
                cs.push(float(i))
            elif i == "+":
                do_des(i)
            elif i == "-":
                do_des(i)
            elif i == "*":
                do_des(i)
            elif i == "/":
                do_des(i)
            else:
                print(cs.top())
def do_des(i):
    l1 = cs.pop()
    l2 = cs.pop()
    cs.push(eval(str(l2)+str(i)+str(l1)))
dcmess()


