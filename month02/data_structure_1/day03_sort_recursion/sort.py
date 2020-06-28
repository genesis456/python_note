"""
sort.py 排序算法训练
"""
list= [4,9,3,1,2,5,8,4]
#冒泡排序
def bubble(list_):
    n =len(list_)
    #外层循环表示比较多少轮
    for i in range(n-1):
        #内层循环表示每轮比较多少次(i是从0开始的，每次比较-1)
        for j in range(n-1-i):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1] = list_[j+1],list_[j]

bubble(list)
print(list)

# 快速排序
def sub_sort(list_,low,high):
    #选定基准(第一个元素4)
    x = list_[low]
    #low向后走，high向前走（low=high表示遍历完一轮）
    while low < high:
        #后面的数往前放
        #如果high向前走(遍历)的数大于基准数，不用管，继续向前遍历走
        while list_[high] > x and high > low:
            high -= 1
        #否则，从后往前遍历的某个数小于基准数，就将那数往前甩
        # （0索引的元素已经赋给了基准，此时已空出来，将要甩的那个数放到0索引那）
        list_[low] = list_[high]
        #发现一个元素比基准小，就前甩。然后执行第二个while
        #前面比基准大往后放
        #开始从0索引那进行第二次循环比较
        while list_[low] <= x and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = x   #最后将基准值插入空缺的位置（也就是中间，左边都比基准值小，右边都比基准大）
    return low
#都是比较你设定的那个基准值,每次比较完一轮，就将基准索引返回作为下一轮的最后元素索引和开头元素索引

def quick(list_,low,high):
    #low 表示第一个元素索引，high表示最后一个元素索引
    #0<7
    if low < high:
        key = sub_sort(list_,low,high)
        quick(list_,low,key - 1)
        quick(list_,key+1,high)

quick(list, 0, len(list) - 1)
print(list)

#选择排序
def selection_sort(list_):
    #每轮选出一个最小值，需要len(list_)-1轮（也就是两两比较需要多少次）
    for i in range(len(list_)-1):
        min = i  #假设min为最小值
        #i的后一个与i比较
        for j in range(i+1,len(list_)):
            if list_[min] > list_[j]:
                min = j
        #一轮确定了一个最小值,再将最小值换到应该在的位置
        if min != i:
            list_[i],list_[min] = list_[min],list_[i]

selection_sort(list,)
print(list)

#插入排序
def insertion_sorting(list_):
    #控制每次比较的数是谁，从第二个开始往前比较，
    # 若后一个数比前面一个数大，就插入在原位，否则，和前一个交换
    for i in range(1,len(list_)):
        x = list_[i]  #空出list_[i]的位置
        j = i-1
        while j >= 0 and list_[j] >x:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1] = x

insertion_sorting(list,)
print(list)