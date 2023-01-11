# N의 각 자릿수의 합을 리턴

result = 0

def SumDigits(n):
  if n < 10:
    return n
  
  return n % 10 + SumDigits(n // 10)

print(SumDigits(22541))