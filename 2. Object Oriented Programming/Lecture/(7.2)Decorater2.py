def AddPrintTo(Original):
  def Wrapper():
    print("|| 함수 시작 ||")
    Original()
    print("|| 함수 끝 ||")
  return Wrapper

@AddPrintTo                           # PrintHello 함수를 AddPrintTo로 Decorate 한다는 의미
def PrintHello():
  print("안녕하세요")

PrintHello()