"""
作者：周乐
日期：22/09/2019
    双for循环练习2:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
"""
# list01 = [3, 80, 45, 5, 80, 1]
# for c in range(1,len(list01)):
#     list01[0]  c


#如果需要退出多重循环体，则需要使用到标记
#假设result　＝False
result = False
list01 = [3, 80, 45, 5, 80, 1]
for r in range(len(list01)-1):
    for c in range(r+1,len(list01)):
        if list01[r] == list01[c]:
            print("有重复的")
            result = True   #若满足这个选择语句，result就变为Ｔrue
            break   #退出循环体
    if result:
        break   #if result等同于if　result = false　判断一个没有重复的就退出循环

print("无重复")
  #这题最大的难点是：　无法判断到一个重复就立马退出，不再继续循环判断（多重循环体，则需要使用到标记）