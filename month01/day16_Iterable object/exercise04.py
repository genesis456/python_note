# 练习：员工管理器记录多个员工
#      迭代员工管理器对象

class Employee:
    pass


class EmployeeManager:
    """
    可迭代对象
    """
    def __init__(self):
        self.__employees = []

    def add_employees(self,person):
        self.__employees.append(person)

    def __iter__(self):
        return EmployeeAtor(self.__employees) #将列表传入EmployeeAtor中

class EmployeeAtor:
    """
    员工迭代器（获取下一个数据的）
    """
    def __init__(self,getar):
        self.__getar = getar
        self.__ater = 0
    def __next__(self):
        if self.__ater > len(self.__getar)-1:
            raise StopIteration
        temp = self.__getar[self.__ater]
        self.__ater += 1
        return temp


manage = EmployeeManager()
manage.add_employees(Employee())
manage.add_employees(Employee())
manage.add_employees(Employee())

#用迭代器遍历
iterator = manage.__iter__()            #模式格式不变，固定好的
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break