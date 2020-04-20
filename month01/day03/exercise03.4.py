"""
  作者：周乐
  日期：１９／０７／２０１９
  if练习4：自学（参照Ｐｙｔｈｏｎ编程书）
  ［三酷猫判断找鱼］
三酷猫经过几天钓鱼，钓上了鲫鱼、鲤鱼、鲢鱼、草鱼、黑鱼、乌龟，在其记账单里记录为鲫鱼5条、鲤鱼8条、鲢鱼7鱼、草鱼2条、黑鱼6条、乌龟1只。
编程要求：
（1）	用字符串记录上述内容。
（2）	检查字符串的长度。
（3）	用条件判断找出三酷猫想要找的乌龟，知道钓了几只，并告诉是奇数还是偶数只。



"""

fish_record = "鲫鱼５条,鲤鱼８条,鲢鱼７条,草鱼２条,黑鱼６条,乌龟１只"
print(len(fish_record))  #len获取字符串长度
if fish_record[0:2] == "乌龟":
    print("是乌龟吗?,是",fish_record[0:2])

elif fish_record[5:7] == "乌龟":
    print("是乌龟吗?,是", fish_record[5:7])

elif fish_record[10:12] == "乌龟":
    print("是乌龟吗?,是", fish_record[10:12])

elif fish_record[15:17] == "乌龟":
    print("是乌龟吗?,是", fish_record[15:17])
elif fish_record[20:22] == "乌龟":
    print("是乌龟吗?,是", fish_record[20:22])
elif not fish_record[25:27] != "乌龟":
    if int(fish_record[27])/2 == 0:
        print("找到乌龟了，是%d只，偶数"%(int(fish_record[27])))
    else:
        print("找到乌龟了，是%d只，奇数" % (int(fish_record[27])))
else:
    print("不存在")