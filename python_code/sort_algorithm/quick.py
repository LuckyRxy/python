# todo: 快速排序
# todo: 快速排序通过选择一个基准元素，将小于基准元素的元素放在左边，大于基准元素的元素放在右边，然后对左右两个部分递归地进行快速排序。
# @Time: 2024/12/28 13:44:29
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

def quick_sort(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 示例
arr = [3, 6, 8, 10, 1, 2, 1]
print("Quick Sort:", quick_sort(arr))