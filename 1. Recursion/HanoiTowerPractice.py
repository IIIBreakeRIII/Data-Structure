# 하노이의 탑 문제
# 진짜 이해하고 싶다

# 코드잇 답

def MoveDisk(DiskNum, StartPeg, EndPeg):
  print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (DiskNum, StartPeg, EndPeg))
  print("움직이는 조건 수행 출력")

def Hanoi(DiskNum, StartPeg, EndPeg):
  if DiskNum == 0:
    print("조건 수행 완료")
    return
  else:
    OtherPeg = 6 - StartPeg - EndPeg            # 2
    Hanoi(DiskNum - 1, StartPeg, OtherPeg)
    print("조건 1 수행")
    MoveDisk(DiskNum, StartPeg, EndPeg)
    print("움직이는 조건 수행")
    Hanoi(DiskNum - 1, OtherPeg, EndPeg)
    print("조건 2 수행")


# Test Code

Hanoi(3, 1, 3)