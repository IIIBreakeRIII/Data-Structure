# List를 거꾸로 뒤집는 함수 구현

def flip(SomeList):
  if len(SomeList) == 0:
    return SomeList
  
  return [SomeList.pop()] + flip(SomeList)

SomeList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
SomeList = flip(SomeList)
print(SomeList)