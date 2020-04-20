"""

编写一个接口程序,要求判断一段文字中括号匹配是否正确,
如果正确则打印"匹配正确",如果不正确则打印出哪里出错(只需要找出第一个错误即可)

出错情况 : 少前括号,少后括号,括号不匹配

"""
####思路： 遍历字符串，遇到左括号就进栈，遇到右括号就把栈中
####左括号出栈与右括号进行匹配
#利用顺序栈
from s_stack import *
text = """When an Open Data (standard) is created and promoted,
it’s [important] to think why - what change is th=is {trying (to) drive}?
What will people do with this data that they couldn’t do before?"""

#将验证条件提前定义好
parens = "(){}[]"   # 特殊处理的字符集
left_parens = "([{"  # 入栈字符集
#验证匹配关系
opposite = {'}':'{',']':'[',')':'('}
st = SStack()  #存储括号的栈

#编写生成器，用来遍历字符串，不断的提供括号及其位置
def parent(text):
    # i 遍历字符串的索引位置
    i,text_len = 0,len(text)

    #  开始遍历字符串
    while True:
        #当索引小于字符串长度（还没遍历到结尾）
        # 并且字符串不属于parens。就向后移动
        while i < text_len and text[i] not in parens:
            i += 1

        #到字符串结尾了（返回值None）
        if i >= text_len:
            return
        else:
            yield text[i],i #将括号及索引返回
            i += 1

# 功能函数判断提供的括号是否匹配
def ver():
    for pr, j in parent(text):
        if pr in left_parens:    #pr:字符  j:位置
            st.push((pr,j)) # 左括号入栈（可以作为元组和索引一起入栈）
        elif st.is_empty() or st.pop()[0] != opposite[pr]:
                            #st.pop()取出的是(pr,j)，拿［0］
            print("Unmatching is found at %d for %s"%(j,pr))
            break  #有错的就告知并退出

    else:
        if st.is_empty():
            print("All parentheses are matched")
        else:
            #左括号多了
            d = st.pop()
            print("Unmatching is found at %d for %s"%(d[1],d[0]))

ver()


