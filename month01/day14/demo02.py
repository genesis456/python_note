"""
    运算符重载
"""

# 算数运算符
class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "一维向量的分量是：" + str(self.x)

    def __add__(self, other):
        return Vector1(self.x + other)

    def __sub__(self,other):
        return Vector1(self.x - other)

    def __mul__(self,other):
        return Vector1(self.x * other)



v01 = Vector1(10)
print(v01 + 2)  # v01.__add__(2)
print(v01 - 2)
print(v01 * 2)


# 反向算数运算符重载(数值和对象位置调换，而运算符函数要加r)
class Vector1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "一维向量的分量是：" + str(self.x)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __rsub__(self,other):
        return Vector1(self.x - other)

    def __rmul__(self,other):
        return Vector1(self.x * other)


v01 = Vector1(10)
print(2 + v01)  # v01.__add__(2)
print(2 - v01)
print(2 * v01)



print(id(v01))
# 重写__iadd__，实现在原对象基础上的变化。
# 如果重写__iadd__,默认使用__add__，一般会产生新对象.
v01 += 2
print(v01,id(v01))


# list01 = [1]
# print(id(list01))
# # 生成新对象
# re = list01 + [2]
# print(re,id(re))
# # 在原有对象基础上，累加.
# list01 += [2]
# print(list01,id(list01))
