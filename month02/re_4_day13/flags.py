"""
flags.py
flags  扩展匹配功能演示
"""
import re

s = """Hello
广东"""

#只能匹配ASCII编码(flags=re.A)
# regex = re.compile(r'\w+',flags=re.A)

#不区分大小写(flags=re.I)  例:验证码不区分大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# .可以匹配换行(flags=re.S)
# regex = re.compile(r'.+',flags=re.S)

# ^,$匹配每一行开头结尾位置(flags=re.M)
regex = re.compile(r'^广东',flags=re.M)


l = regex.findall(s)
print(l)