
from bll import *
from model import *
class StudentManagerView:
    """
     学生管理器视图
    """
    def __init__(self):
        self.__manager = StudentManagerController()  #由于只调用一次，所以放在数据成员这即可

    def __display_menu(self):
        """
        显示菜单
        """
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        """
        选择菜单项
        """
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()




    def __manage_error(self,message):
        """
        处理错误的方法（可能出现的错误都可以在这调用）
        :param message: 可能出现的错误
        :return: 处理结果
        """
        while True:
            try:
                number = int(input(message))
                return number
            except:
                # continue
                print("输入有误，请重新输入")   #客户体验感


    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        """
        输入学生信息
        """
        name = input("请输入姓名：")

        age = self.__manage_error("请输入年龄：")  #调用上面处理错误的函数，返回处理的结果

        score = self.__manage_error("请输入成绩：")      #处理错误和上面只是数据不同，所以可以放在同一方法中

        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self,list_output):
        """
        输出学生信息
        """
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        """
        删除学生信息
        :return:确认信息
        """
        id = self.__manage_error("请输入编号：")  #调用处理错误方法

        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        """
        修改学生信息
        :return: 确认信息
        """
        stu = StudentModel()  #自定义一个对象调用信息模型

        stu.id = self.__manage_error("请输入需要修改的学生编号:")  #调用处理错误方法

        stu.name = input("请输入新的学生名称：")
        stu.age = self.__manage_error("请输入新的学生年龄：")   #调用处理错误方法

        # stu.score = int(input("请输入新的学生成绩："))
        stu.score = self.__manage_error("请输入新的学生成绩：")  #调用处理错误方法
        if self.__manager.update_student(stu):
            print("修改成功")

        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)