# 1부터 N까지의 합을 Return

def TriangleNum(n):
  if n == 1:
    return 1
  else:
    return TriangleNum(n - 1) + n

for i in range(1, 11):
  print(TriangleNum(i))