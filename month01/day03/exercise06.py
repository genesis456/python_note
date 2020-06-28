"""
作者：周乐
日期：２０／０８／２０１９
    while计数
"""


count = 0 #初始值是０开始
while count < 3: #重复三次（计数０，１，２）
    count += 1 #每次在自身加一
    usd = int(input("请输入美元："))
    print(usd * 6.9)