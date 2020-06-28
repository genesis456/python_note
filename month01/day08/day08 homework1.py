"""
作者：周乐
日期：26/10/2019
自学(参照菜鸟教程)字符串/列表/字典常用函数(方法),实现如下功能。
    字符串："　校　训：自　强不息、厚德载物。　　"
    查找空格的数量
    删除字符串前后空格
    删除字符串所有空格
    查找"载物"的位置
    判断字符串是否以"校训"开头.

 """
# str_unit = "　校　训：自　强不息、厚德载物。　　"
# startswith("校训",str_unit)
# sub = ""
# str_unit.count(sub)
# str_unit.rstrip() #删除末尾字符，默认是空格
# str_unit.strip()　　#删除前后字符，默认空格
# str_unit.replace(" ","")　　＃替换函数，将空格换成无符号
# str01.index("载物")　　＃寻找字符串的索引位置
str01 = "　校　训：自　强不息、厚德载物。　　"

print(str01.count("　"))  #注意中英文空格
str02 = str01.rstrip().lstrip()
print(str02)  #删除末尾字符加删除最左边的字符（等同于删除前后字符）
str03 = str01.replace("　", "")   #注意空格中英文符
print(str03)
print(str01.index("载物"))
print(str01.startswith("校训"))











