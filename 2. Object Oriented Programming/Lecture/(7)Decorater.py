def PrintHello():
  print("안녕하세요")

def AddPrintTo(Original):
  def Wrapper():
    print("|| 함수 시작 ||")      # 부가 기능
    Original()            # PrintHello 호출과 동일
    print("|| 함수 끝 ||")        # 부가 기능
  return Wrapper

# 어떤 함수를 받아서 또 다른 함수를 리턴하는 구조
# PrintHello -> Original
AddPrintTo(PrintHello)()

# 다음과 같이도 가능
PrintHello = AddPrintTo(PrintHello)
PrintHello()