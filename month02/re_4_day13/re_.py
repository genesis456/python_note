"""正则表达式练习"""
#匹配一个.com邮箱的格式字符串
import re
email = input("请输入邮箱地址：")
res = re.findall(r'\w+@\w+\.com$',email)  #必须加$，不然多加一个com都不会报错(不严谨)
if res:
    print("输入成功%s" % email)
else:
    print("输入有误，请重新输入")


#匹配一个密码，8-12位数字字母下划线构成
import re
password = input("请输入密码：")
res = re.findall(r'[a-zA-Z0-9_]{8,12}',password)  #如果写\w{8，12}的话，不严谨。密码不能中文汉字
if res:
    print("输入成功%s" % password)
else:
    print("输入有误，请重新输入")


#匹配一个数字，正数，负数，整数，小数，分数1/2，百分数45%
import re
res = '12, 15, -45, 0, 1.34, 5/6, 56%,hh,哇,#$'
st = re.findall(r'-?\d+/?\.?\d*%?',res)  # - . / % 都是可有可无，0是表示第二部分数字用*表示，可没有可多个
print(st)

#匹配一段文字中以大写字母开头的单词，注意文字中
#可能有 iPython(不算）  H-base(算），单词可能有 大写字母 小写字母 -_

import re
msg = """In this column, we will iPython have a section called Wit and Fun, in which we will present some English puzzles,
humorous stories and games. We will also have a section called Tips on Learning English,
where you can share your successful  Me--too learning experience with others. Besides, in the section — I Say, You Say,
different  UFO opinions  I on hot topics and phenomena will be warmly welcome.
Please send your contributions to the E_ditorial Section or e-mail to: englishcolumn@sina.com.cn. Please remember:
contributions are expected to be within 500 words.
"""
st = re.findall(r'\b[A-Z][a-zA-Z-_]*',msg)  #将上\b，iPython就不会匹配到。每个单词左边有个边界
print(st)

