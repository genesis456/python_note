"""
作者：周乐
日期：０１／０９／２０１９
day03作业2：
   在控制台中获取年龄:
如果小于0岁，打印有误
如果一个人的年龄小于2岁，就打印一条消息指出他是婴儿。
如果一个人的年龄为2（含）~13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）~20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）~65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁~150岁，就打印一条消息，指出他是老年人。
150岁以上，打印“那不可能”

"""
age = int(input("请输入年龄："))
if age < 0:
    print("打印有误")
elif age < 2:           #因为那些年龄小的之前已经判断过了，所有后面自然不需要判断了
    print("婴儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
elif age < 150:
    print("老年人")
else:
    print("那不可能")