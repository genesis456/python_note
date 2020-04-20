# 5. 以万物皆对象的思想，洞察客观实物，
#    随意创建两个类，四个对象，并调用其方法.

class Teacher:  #类名首字母要大写
    #数据成员
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #行为成员
    def prelection(self):
        """
        讲课
        """
        print(self.name+"讲课" )

tea01 = Teacher("凌小姐","18")
tea01.prelection()

class Gril:
    def __init__(self,smile,tall):
        self.smile = smile
        self.tall = tall
    def call(self):
        """
      打电话
        """
        print(self.smile + "打电话")

sm = Gril("微笑",174)
sm.call()