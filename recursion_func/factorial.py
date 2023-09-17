# Factorial Algorithm

# using for - repeat
def factorial_repeat(num):

    result = 1
    
    for i in reversed(range(1, num + 1)):
        result = result * i

    return result

# using recursion function
def factorial_recursion(num):

    if num == 1:
        return 1
    
    return num * factorial_recursion(num - 1)
    

print(factorial_repeat(5))
print(factorial_recursion(5))
