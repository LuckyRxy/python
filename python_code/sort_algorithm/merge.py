# todo: 归并排序
# todo: 归并排序通过将两个有序的子序列合并成一个有序序列，递归地进行这个过程，直到整个序列有序。
# @Time: 2024/12/28 13:48:37
# @Author: xiangyang.ren
# @Email: yalile1011@gmail.com

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 示例
arr = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort:", merge_sort(arr))
