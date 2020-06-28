"""
作者：周乐
日期：０１／０９／２０１９
day03作业3：
 根据身高体重，参照BMI，返回身体状况。
BMI :用体重千克数除以身高米数的平方得出的数字
中国参考标准：
体重过低 BMI < 18.5
正常范围 18.5≤BMI < 24
超重24≤BMI < 28
I度肥胖 28≤BMI <30
II度肥胖30≤BMI < 40
III度肥胖BMI ≥ 40.0

"""
tall = float(input("请输入身高（米）："))
weight = float(input("请输入体重（千克）："))
BMI = weight / tall**2

if BMI < 18.5:
    print("体重过低")
elif BMI < 24:
    print("正常")
elif BMI < 28:
    print("超重")
elif BMI < 30:
    print("I度肥胖")
elif BMI < 40:
    print("II度肥胖")
else:
    print("III度肥胖")