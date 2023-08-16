# Linear Search

def linear_search(num_list, key):
    for i in range(len(num_list)):
        if num_list[i] == key:
            return i + 1 
    return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search(numbers, 6))
print(linear_search(numbers, 20))
