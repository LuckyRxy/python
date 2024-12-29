# todo: 插入排序
# todo: 插入排序通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
# @Time: 2024/12/28 13:38:19
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr