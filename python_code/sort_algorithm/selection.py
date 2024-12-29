# todo: 选择排序
# todo: 选择排序通过在未排序部分中选择最小元素并将其放置在未排序部分的开头。
# @Time: 2024/12/28 13:34:44
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i # 记录最小元素的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 示例
arr = [64, 25, 12, 22, 11]
print("Selection Sort:", selection_sort(arr))
