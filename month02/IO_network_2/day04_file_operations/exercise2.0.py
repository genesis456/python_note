"""
作者：周乐
日期：2020/2/21
exercise2.0升级
"""

try:
    f = open('English_dict')
except Exception as e:
    print(e)
# 每次获取一行
else:
    while True:
        f.seek(0)
        word = input("Word:")
        if not word:
            break
        for line in f:
            #以空格将前后分割，取最前面的
            w = line.split(' ')[0]
            # 如果遍历到的单词已经大于目标,就结束查找
            if w > word:
                print("没有找到该单词")
                break
            elif w == word:
                print(line)
                break
        else:
            print("没有找到单词")

    f.close()