"""
作者：周乐
日期：29/11/2019
   可迭代对象练习2:
        不使用for，获取字典所有数据。
        {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
"""

dict01 = {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
iterator = dict01.__iter__()  #获取可迭代对象
while True:
    try:
        key = iterator.__next__()
        print(key,dict01[key])       #回到字典那看看怎么通过键拿值
    except StopIteration:
        break