# Recursion Function Example

def recursion(num):
    if num == 0:
        return

    print(num, "| Recursion")
    num -= 1
    recursion(num)

recursion(5)
