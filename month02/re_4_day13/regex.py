"""
regex.py re模块  功能函数演示
"""
import re

# 目标字符串
s = 'Alex:2000,Sunny:1999'
pattern = r'\w+:\d+'  #正则表达式

#re 模块调用findall
l = re.findall(pattern,s)
print(l)

#compile 对象调用findall
regex = re.compile(pattern)
l = regex.findall(s,0,12)   #regex的findall中pos，endpos参数是截取目标字符串的开始与结束匹配位置
print(l)


#按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]',s)  #按：和，对字符串进行切割
print(l)


#替换目标字符串
s = re.sub(r':','-',s)
print(s)  # 返回值: 替换后的字符串


