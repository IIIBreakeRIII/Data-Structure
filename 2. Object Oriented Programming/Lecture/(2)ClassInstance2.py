class User:
  def SayHello(SomeUser):

    # 인사 메시지 출력 메서드
    print("안녕하세요! 저는 {}입니다!".format(SomeUser.name))

  def login(SomeUser, MyEmail, MyPassword):

    # 로그인 메서드
    if(SomeUser.email == MyEmail and SomeUser.password == MyPassword):
      print("로그인 성공, 환영합니다!")
    else:
      print("로그인 실패!")

user1 = User()

user1.name = "jeeon"
user1.email = "jeeon@email.com"
user1.passwrod = "12345"

user1.login(user1, "jeeon@email.com", "12345")    # 다음과 같이 전달하면 오류
user1.login("jeeon@email.com", "12345")           # 이 방법이 맞음

# 인스턴스 이름으로 메서드를 호출할 경우, 파라미터에 인스턴스 이름이 들어가게 되면 중복되어 호출됨. 즉, 다음과 같음
# User.login(user1, user1)    =>    클래스이름.메서드이름(인스턴스 변수, 인스턴스 변수)
# 때문에 인스턴스 변수명으로 호출 시, 파라미터에는 넘겨는 값만 들어가면 됨