"""
struct模块进行数据打包
"""

from struct import *

#1 lisi 1.75
st = Struct('i4sf')  #类型结构(1是整型i,lisi是4位字符串，1.75是浮点型)
data = st.pack(1,b'lisi',1.75)  #字符串要转为字节串发送
print(data)
print(st.unpack(data))  #将数据解析