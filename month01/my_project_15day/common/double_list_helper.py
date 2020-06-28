class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_return(self):
        print("asdfghjkl")


import sys   #(仅当扩展知识)　　　　　＃＃＃＃将查看导包的语法放在主模块导其他模块的前面
# 如果不再pycharm中运行当前模块，则导包失败.
# 将项目根目录加入path中，导包才会成功.
sys.path.append("/home/tarena/1906/month01/code/my_project_15day")
print(sys.path)

# 4.	在double_list_helper.py中调用main.py。
from main import fun1   #运行正确，但显示红线，是因为内部调外部没标记
fun1()


