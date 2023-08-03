# 하노이의 탑 문제
# 진짜 이해하고 싶다

# 코드잇 답

def MoveDisk(DiskNum, StartPeg, EndPeg):
  print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (DiskNum, StartPeg, EndPeg))

def Hanoi(DiskNum, StartPeg, EndPeg):
  if DiskNum == 0:
    return
  else:
    OtherPeg = 6 - StartPeg - EndPeg
    Hanoi(DiskNum - 1, StartPeg, OtherPeg)
    MoveDisk(DiskNum, StartPeg, EndPeg)
    Hanoi(DiskNum - 1, OtherPeg, EndPeg)

# Test Code

Hanoi(3, 1, 3)