"""
2　0　4　8核心算法
"""
#最重要的是思想（和面试官谈2048项目，不要揪细节，讲主要思想思路）
# :这个游戏无论是左右移还是上下移，行与行，列与列之间的逻辑毫不相干，
# 但他们的逻辑又那么的相似（甚至可以说是一样的），所以对于这种二维游戏，
# 当然用这种二维列表来表达它的核心算法，但发现行与行，列与列互不干扰，
#所以我将左右移上下移用一种降维的思想（降维指一个二维问题降为一维），
# 我将二维想成一个一维的．这时候只有左右，没有上下．而无论是上还是下，左还是右．
#只处理一维列表，而不思考二维列表，在不同游戏有不同降发．而在2048游戏中，
# 将左右变为一维列表，而上下则利用方阵转置思想．（上下移是转置后变成了一个只有左右移的一维问题）
#现在就可以考虑左右合并的问题了，（左右移时）而中间出现0的先去出来，然后所有数据是挨着的，
# 发现相邻的数相同的话就将后一个加给前一个，后一个就删除并在后面补0．
# 最后再进行一次方阵转置，还原原先的二维列表．这就是整个2048游戏的核心算法思想．


#练习1：
#[2,0,2,0]  -->  [2,2,0,0]
list_merge = None
def zero_to_end():
    """
    零元素移到末尾
    """
    #思想：从后向前，如果发现零元素，删除并末尾追加

    # print(list_merge)   #如果调试没查出来问题在哪，
    # 就在每个阶段那print打印看看是否正确．慢慢缩小范围
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0 :
            del list_merge[i]
            list_merge.append(0)

# zero_to_end()
# print(list_merge)

#练习２:将相同的元素进行合并
#  [2,2,0,0]  -->  [4,0,0,0]   (相邻一样的元素合并)
#　[2,0,0,2]  -->  [4,0,0,0]
#　[2,0,4,0]  -->  [2,4,0,0]
#　[2,2,2,0]  -->  [4,2,0,0]

def merge_same_number():
    """
    合并
    """
    #先将中间的零元素移到末尾
    #再合并相邻相同的元素
    zero_to_end()
    for j in range(len(list_merge)-1):
        if list_merge[j] == list_merge[j+1]:
            #将后一个累加前一个之上
            list_merge[j] += list_merge[j+1]
            #删除后一个，并补0
            del list_merge[j+1]
            list_merge.append(0)
    # print(list_merge) 此阶段没有问题

# merge_same_number()
# print(list_merge)

#练习３：地图向左移动
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
def move_left():
    """
    向左移动
    """

    #思想：将二维列表中每行交给merge函数进行操作
    for line in map:
        global list_merge  #在局部想要改变全部变量，前面要加global
        list_merge = line   #将大列表中的每个小列表元素传给list_merge
        merge_same_number()

def move_right():
    """
    向右移动
    """

    #思想：将二维列表中每行（从右向左）交给merge函数进行操作
    for line in map:
        global list_merge  # 在局部想要改变全部变量，前面要加global
        list_merge = line[::-1]  ######从右向左取出数据，形成新列表，
                  ##########list_merge 执行完后要赋值给原来的line列表才行＃＃＃
        merge_same_number()   #第二个元素结束是4　8　0　0
        #从右向左接收　　合并后的数据　　　0　0　8　4　
        line[::-1] = list_merge


# move_right()
# print(map)

#练习４：向上移动　　向下移动
#提示：　利用方阵转置函数
#大体思路和左右移动是一样的

def move_upward():
    """
   向上移动
   利用方阵转置

    """
    square_transpose(map)  #（转置完向左移）
    move_left()
    square_transpose(map)  #再进行转置还原

def move_down():
    """
   向下移动
   利用方阵转置

    """
    square_transpose(map)  # （转置完向右移）
    move_right()
    square_transpose(map)  # 再进行转置还原


def square_transpose(list01):
    """

    :return: 方阵转置
    """
    for c in range(1, len(list01)):
        for r in range(c, len(list01)):
            list01[r][c-1], list01[c-1][r] = list01[c-1][r], list01[r][c-1]
# move_upward()
# print(map)


move_down()
print(map)







