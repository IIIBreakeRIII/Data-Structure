# Index Sequential Search
# 색인 순차 탐색

num_list = [3, 9, 15, 22, 31, 55, 67, 88, 91]
index_table = [[0, 3], [2, 15], [6, 67]]

index_size = len(index_table)

def sequential_search(key, low, high):
    for i in range(low, high, 1):
        if num_list[i] == key:
            print("Index number :", i, "Key :", key)
            return i

    return -1

def index_search(key):

    i, low, high = 0, 0, 0

    if key < num_list[0] or key > num_list[len(num_list) - 1]:
        return -1
    
    for i in range(0, index_size, 1):
        if i < index_size - 1:
            if index_table[i][1] <= key and index_table[i + 1][1] > key:
                break
        elif i == index_size - 1:
            if index_table[i][1] >= key:
                break

    if i == index_size - 1:
        low = index_table[i - 1][0]
        high = len(num_list)

    else:
        low = index_table[i][0]
        high = index_table[i + 1][0]

    return sequential_search(key, low, high)


index_search(31)
