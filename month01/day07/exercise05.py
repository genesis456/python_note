"""
作者：周乐
日期：19/09/2019
集合练习2: 经理：曹操,刘备,孙权
      技术：曹操,刘备,张飞,关羽
请计算：
     (1)是经理也是技术的有谁？
     (2)是经理，不是技术的有谁?
     (3)是技术，不是经理的有谁?
     (4)张飞是经理吗?
     (5)身兼一职的都有谁?
     (6)经理和技术总共有都少人?
"""
set01 = {"曹操","刘备","孙权"}
set02 = {"曹操","刘备","张飞","关羽"}

print("是经理也是技术的有:", set01 & set02)
print("是经理，不是技术的有", set01 - set02)
print("是技术，不是经理的有:",set02 - set01)
print("张飞" in set01)
print("身兼一职的都有:", set01 ^ set02)
print(len(set01 | set02))