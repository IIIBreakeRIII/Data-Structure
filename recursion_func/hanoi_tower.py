# Hanoi Tower Algorithm

def hanoi_tower(n, start, temp, to):
    if n == 1:
        print("No. 1 disk moves from", start, "to", to)
    else:
        hanoi_tower(n - 1, start, to, temp)
        print("No.", n, "disk moves from", start, "to", to)
        hanoi_tower(n - 1, temp, start, to)

hanoi_tower(3, "A", "B", "C")
