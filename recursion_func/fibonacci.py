# Fibonacci Algorithm

def fibonacci_for(num):

    fib1, fib2, fib3 = 0, 1, 0

    for i in range(2, num):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3

    return fib3

def fibonacci_recursion(num):
    
    if num == 1:
        return 0
    elif num == 2:
        return 1

    return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2)

print("Fibonacci Using for =", fibonacci_for(10))
print("Fibonacci Using Recursion =", fibonacci_recursion(10))
