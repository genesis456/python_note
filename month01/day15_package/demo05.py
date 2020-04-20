"""
    自定义异常类
"""
class AgeError(Exception):
    """
        年龄错误
    """
    def __init__(self,message,age_value,code_line,error_number):
        super().__init__("出错啦啦啦")   #子类要调用父类的构造函数
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Wife:
    def __init__(self,age):  #错误到这并不处理，继续往上抛
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 21 <= value <= 31:
            self.__age = value
        else:
            # 5
            # raise ValueError("我不要")　  #这个只能是被规定好了的
            #出错之后会将错误往上抛，
            raise AgeError("超过我想要的范围啦",value,26,1001)  #自定义一个异常类，加入需要的参数

# w01 = Wife(81)   #错误的根源（用异常处理的方法解决）
try:
    w01 = Wife(81)
except AgeError as e:
    print("请重新输入")
    print(e.message)
    print(e.age_value)
    print(e.code_line)

