# 파이썬에서는 인스턴스 메서드의 첫번째 파라미터 이름을 self로 사용하라고 권장
# self가 아닌 다른 단어도 상관없음

class User:
  def SayHello(self):

    # 인사 메시지 출력 메서드
    print("안녕하세요! 저는 {}입니다!".format(self.name))

  def login(self, MyEmail, MyPassword):

    # 로그인 메서드
    if(self.email == MyEmail and self.password == MyPassword):
      print("로그인 성공, 환영합니다!")
    else:
      print("로그인 실패!")

user1 = User()

user1.name = "jeeon"
user1.email = "jeeon@email.com"
user1.passwrod = "12345"

user1.login("jeeon@email.com", "12345")