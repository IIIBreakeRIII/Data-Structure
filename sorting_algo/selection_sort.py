# Selection Sorting Algorithm
# 선택 정렬 알고리즘

def selection_sort(num_list):

    index, temp = 0, 0

    for i in range(len(num_list)):
        min_value = 100

        for j in range(i, len(num_list)):
            if num_list[j] < min_value:
                min_value = num_list[j]
                index = j

        temp = num_list[i]
        num_list[i] = num_list[index]
        num_list[index] = temp

    return num_list

num_list = [9, 6, 1, 3, 5]
print(selection_sort(num_list))
