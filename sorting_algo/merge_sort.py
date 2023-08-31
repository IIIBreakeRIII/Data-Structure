# Merge Sort Algorithm

def merge(num_list, left, right):
    temp_list = []
    mid = (left + right) // 2
    L = left
    R = mid + 1

    while L <= mid and R <= right:
        if num_list[L] <= num_list[R]:
            temp_list.append(num_list[L])
            L += 1
        else:
            temp_list.append(num_list[R])
            R += 1

    while L <= mid:
        temp_list.append(num_list[L])
        R += 1

    while R <= right:
        temp_list.append(num_list[R])
        R += 1

    for i in range(left, right + 1):
        num_list[i] = temp_list[i - left]

    return num_list


def merge_sort(num_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(num_list, left, mid)
    merge_sort(num_list, mid + 1, right)
    return merge(num_list, left, right)

num_list = [5, 3, 2, 7, 8, 1, 9, 0, 6, 4]
merge_sort(num_list, 0, 9)
print(num_list)
