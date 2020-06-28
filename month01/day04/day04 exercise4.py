"""
作者：周乐
日期：10/09/2019
    (扩展)一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共"弹起来"多少次（最小弹起高度0.01ｍ）．
            总共走了多少米

"""

height = 100
count = 0
distance = height  #可以先把初始距离给它
# 弹起前高度 大于　最小弹起高度
# while height > 0.01:
# 弹起来的高度 大于　最小弹起高度（我们需要的是弹起来的）
while height / 2 > 0.01:
    count += 1
    #弹起
    height /= 2
    print("第%d次弹起来的高度是%f." % (count, height))

    # 累加起/落高度(不要忽略落下去的高度)
    distance += height * 2

print("总共弹起来%d次" % count)
print("总共走了%.2f米" % distance)






