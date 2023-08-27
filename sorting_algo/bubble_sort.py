# Bubble Sort Algorithm
# 버블 정렬 알고리즘

def bubble_sort(num_list):
    
    for i in range(0, len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp

    return num_list

num_list = [9, 6, 1, 3, 5]
print(bubble_sort(num_list))
