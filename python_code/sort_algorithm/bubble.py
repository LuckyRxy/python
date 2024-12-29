# todo: 冒泡排序
# todo: 冒泡排序通过比较相邻的元素并交换它们的位置，直到整个序列有序。
#       每次遍历都会将当前未排序部分的最大元素"冒泡"到最后。
# @Time: 2024/12/28 13:20:17
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr

# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(arr))