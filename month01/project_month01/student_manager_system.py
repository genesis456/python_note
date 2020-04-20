"""
    学生管理系统
    项目计划：
        	1.完成数据模型类StudentModel
        	2.创建逻辑控制类StudentManagerController
		    3.完成数据：学生列表 __stu_list
		    4.行为：获取列表 stu_list,
		    5.添加学生方法 add_student
		    6.删除学生remove_student
		    7.修改学生update_student
"""

######实例方法调用时，需给实例方法的类自定义一个对象，然后用对象．实例方法＃＃＃＃＃＃＃＃####


# 	数据模型类：StudentModel
# 		数据：编号 id,姓名 name,年龄 age,成绩 score
# 	逻辑控制类：StudentManagerController
# 		数据：学生列表 __stu_list
# 		行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，修改学生update_student，根据成绩排序order_by_score。
# 	界面视图类：StudentManagerView
# 		数据：逻辑控制对象__manager
# 		行为：显示菜单__display_menu，选择菜单项__select_menu，入口逻辑main，
# 输入学生__input_students，输出学生__output_students，删除学生__delete_student，修改学生信息__modify_student，按成绩输出学生__output_student_by_score

class StudentModel:
    """
    学生信息模型
    """
    def __init__(self,name="",age=0,score=0,id=0):  #默认参数从右往左写
        """
        创建学生对象
        :param name: 姓名，str
        :param age: 年龄，int
        :param score: 成绩,float
        :param id: 编号（该学生对象的唯一标识）
        """


        self.name = name
        self.age = age
        self.score = score
        self.id = id

class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理
    """

    __init_id = 1000   #类变量，表示初始编号（可以被所有对象所共享）,加两下划线表示外部不能用
    def __init__(self):      #由于学生列表是由内部的决定的，而不是由外部执行者决定
        self.__stu_list = []    #数据：学生列表


    @property
    def stu_list(self):     #获取列表也可以用行为成员，但属性更方便
        """
        学生列表
        :return: 存储学生对象的列表
         """
        return self.__stu_list

    def add_student(self, stu_info):     #将学生信息添加到列表中
        """
        添加学生信息
        """

        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self): #只能内部修改，要加双下划线
        """

        编号每次加１
        :return:加好的结果
        """
        StudentManagerController.__init_id += 1  # 上面是类变量（要用类来点info_id）
        return StudentManagerController.__init_id  # 将加１的结果赋给stu_info.id

    def remove_student(self,id):
        """
        根据ｉd移除学生信息
        :param id: 　学生id编号
        :return: 确认信息
        """
        for item in self.__stu_list:  #列表要用对象self点列表
            if item.id == id:
                self.__stu_list.remove(item)  #不能用del，因为不能完全删除元素．要用列表加ｒｅｍｏｖｅ
                return True
        return False

    def update_student(self,stu_info):
        """
        根据id修改学生信息
        :param stu_info: 外部要修改的编号
        :return: 确认信息
        """
        #根据stu_info修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:  #根据id修改元素，如果外部要改的元素ｉd和列表中的id相同，则修改那个
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
        按学生成绩升序排列
        """
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]


""" 测试添加学生功能
manager = StudentManagerController()
s01 = StudentModel("周乐",18,98)
manager.add_student(s01)
for item in manager.stu_list:
    print(item.name,item.id)
"""

""" 测试删除学生功能
manager = StudentManagerController()
manager.add_student(StudentModel("周乐",18,98))
manager.add_student(StudentModel("凌小姐",18,90))
print(manager.remove_student(1002))
for item in manager.stu_list:
    print(item.name,item.id)
"""
"""测试修改学生信息功能
manager = StudentManagerController()
manager.add_student(StudentModel("周乐",18,98))
manager.add_student(StudentModel("凌小姐",18,90))
for item in manager.stu_list:
    print(item.name,item.age,item.score,item.id)
manager.update_student(StudentModel("宛姑娘",20,94,1002))
print("修改中...")
for item in manager.stu_list:
    print(item.name, item.age, item.score, item.id)
"""

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
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
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
        id = int(input("请输入编号："))
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
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入新的学生名称：")
        stu.age = int(input("请输入新的学生年龄："))
        stu.score = int(input("请输入新的学生成绩："))
        if self.__manager.update_student(stu):
            print("修改成功")

        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudentManagerView()
view.main()