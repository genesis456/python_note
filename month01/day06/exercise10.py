"""
练习:在控制台中录入多个人的多个喜好,输入空字符停止.
例如:请输入姓名：-
    请输入第1个喜好：
    请输入第2个喜好：
    ...
    请输入姓名：
    ...
   最后在控制台打印所有人的所有喜好.

    {“无忌”:[喜好,喜好,喜好]}

"""
dict1 = {}  #先创建一个最外面的字典
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict1[name] = []   #先定位键name，再将［］作为值一起添加到字典中

    count = 1
    while True:

        like = input("请输入第%d个喜好：" % count)
        count += 1
        if like == "":
            break
        dict1[name].append(like)  #往字典的值中添加，定位name键＋append(值)
                                    #这次添加不能使用dict1[name] = like,这样重复多次就变成修改了

for name,like in dict1.items():
    print("%s喜欢：" % name)
    for item in like:
        print(item)
