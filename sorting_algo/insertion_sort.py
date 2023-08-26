# Insertion Sort Algorithm
# 삽입 정렬 알고리즘

def insertion_sort(num_list, n):

    key = 0

    for i in range(1, len(num_list)):
        key = num_list[i]
        print(key)
        
        for j in range(i, 0, -1):
            if num_list[j - 1] > num_list[j]:
                num_list[j - 1], num_list[j] = num_list[j], num_list[j - 1]

    return num_list

num_list = [9, 6, 1, 3, 5]
print(insertion_sort(num_list, len(num_list)))
