# Quick Sort Algorithm
# 퀵 정렬 알고리즘

def quick_sort(num_list, left, right):
    L, R = left, right
    temp = 0
    pivot = num_list[(L + R) // 2]

    while L <= R:
        while num_list[L] < pivot:
            L += 1
        while num_list[R] > pivot:
            R -= 1

        if L <= R:
            if L != R:
                temp = num_list[L]
                num_list[L] = num_list[R]
                num_list[R] = temp
            L += 1
            R -= 1

    if left < R:
        quick_sort(num_list, left, R)
    if L < right:
        quick_sort(num_list, L, right)

    return num_list

num_list = [5, 2, 3, 6, 1, 9, 0, 7, 8, 4]
print(quick_sort(num_list, 0, 9))
