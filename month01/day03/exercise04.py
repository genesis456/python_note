"""
    真值表达式
    ｉｆ　数据：
        语句
    本质就是使用bool函数
    条件表达式

"""
#真值表达式
if "a":
    #等同于if bool("a")，bool(数据)只要里面的数据有值就是ｔｒｕｅ可以执行
    print("真值")

str_input = input("请输入：")
if str_input:
    print("输入的字符串不是空的")



#2. 条件表达式  :有选择性为变量赋值
sex = None   #先给sex赋一个空值，占位作用
if input("请输入性别：") == '男':
    sex = 1
else:
    sex = 0
print(sex)

"""
上述代码优化
"""
sex = 1 if input("请输入性别：") == "男" else 0
print(sex)
# 代码行数节省了３行