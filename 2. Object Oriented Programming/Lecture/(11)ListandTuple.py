MutableObject = [1, 2, 3]
ImmutableObject = (1, 2, 3)

MutableObject[0] = 4
print(MutableObject)

# ImmutableObject[0] = 4              # 튜플은 불변 타입
# print(ImmutableObject)

TupleX = (6, 4)                       # 전체 튜플을 수정하는 것은 가능

TupleX = (4, 1)
Tuplex = (4, 1, 7)

print(TupleX)

listX = []                            # 리스트의 경우 수정 가능

listX.append(4)
listX.append(1)
listX.append(7)

print(listX)
