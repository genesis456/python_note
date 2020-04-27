list0 = [4,9,3,1,2,5,8,4]
#冒泡
def bubble(list0):
    n = len(list0)
    for i in range(n-1):  #比较多少论
        for j in range(n-1-i):
            if list0[j] > list0[j+1]:
                list0[j],list0[j+1] = list0[j+1],list0[j]

bubble(list0)
print(list0)


# def partition(arr,low,high):
#     i = (low-1)
#     pivot = arr[high]
#
#     for j in range(low,high):
#
#         if arr[j] <= pivot:
#             i +=1
#
#             arr[i],arr[j] = arr[j],arr[i]
#
#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return (i+1)
#
#
#
# #快排
# def sub_sort(list0,low,high):
#     if low < high:
#         pi = partition(list0,low,high)
#         sub_sort(list0,low,pi-1)
#         sub_sort(list0,pi+1,high)
#
# sub_sort(len(list0),0,len(list0)-1)
# print(list0)



#快排
# def quick(list0,low,high):
#     if low < high:  #第一个元素索引小于最后一个元素索引时
#         key = sub_sort(list0,low,high)
#         quick(list0,low,key+1)
#         quick(list0,key-1,high)
#
#
#
# def sub_sort(list0,low,high):
#     x = list0[low]
#     while low < high:
#         while list0[high] > x and low <high:
#             high -= 1
#         list0[low] = list0[high]
#         while list0[low] <= x and high >low:
#             low += 1
#         list0[high] = list0[low]
#     list0[low] = x
#     return low

#选择排序
# def selection_sort(list0):
#     for i in range(len(list0)-1):  #比较多少轮次
#         min = i   #假设min为最小值
#         for j in range(i+1,len(list0)):
#             if list0[min] > list0[j]:
#                 min = j
#         if min != i:
#             list0[i],list0[min] = list0[min],list0[i]
# selection_sort(list0)
# print(list0)

#[4,9,3,1,2,5,8,4]
def search(target,val):
    low = 0
    high = len(target)-1
    while low <= high:
        mid = (low+high) // 2
        if target[mid] < val:
            low = mid+1
        elif target[mid] > val:
            high = mid-1
        else:
            return mid






search(list0,3)

