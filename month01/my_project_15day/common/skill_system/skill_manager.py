class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_return(self):
        print("asdfghjkl")

    @staticmethod
    def run():
        print("运行结果")

re = person("zl", 18)



# 3.	在skill_manager.py中调用double_list_helper.py。
from common.double_list_helper import person
vc = person("zl",18)
vc.get_return()