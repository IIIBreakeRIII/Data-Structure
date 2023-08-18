# Binary Search

def binary_search(num_list, key):

    num_list.sort()

    start = 0
    last = len(num_list) - 1
    count = 0

    while start <= last:
        middle = (start + last) // 2

        if num_list[middle] == key:
            count += 1
            print("Search Count =", count)
            return middle

        elif num_list[middle] < key:
            start = middle + 1
            count += 1

        else:
            last = middle - 1
            count += 1

    return -1

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(num_list, 4)
