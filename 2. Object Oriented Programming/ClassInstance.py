# 클래스 생성
class User:
  
  # 내부 속성과 행동 작성
  # 인스턴스 메소드 작성
  def SayHello(SomeUser):         # 함수 정의 -> SomeUser라는 파라미터에는 유저 인스턴스를 넣어주면 됨(ex. user1, user2, etc.)
    
    # 인사 메시지 출력 메소드
    print("안녕하세요! 저는 {}입니다!".format(SomeUser.name))

#인스턴스 호출
user1 = User()
user2 = User()
user3 = User()

# 인스턴스에 속성 추가  =>  인스턴스 이름.속성 이름(인스턴스 변수) = 속성에 넣을 값
# name, email, password = 인스턴스 변수
user1.name = "Paul"
user1.email = "paul@email.com"
user1.password = "12345"

user2.name = "Jonny"
user2.email = "jonny@email.com"
user2.password = "13579"

user3.name = "Luna"
user3.email = "luna@email.com"
user3.password = "02468"


# 각 인스턴스 속성 출력

# print(user1.email)
# print(user2.password)


# 인스턴스 메소드 출력
# 클래스 이름.메서드 이름(인스턴스)
# 클래스의 메서드를 호출

User.SayHello(user1)
User.SayHello(user2)
User.SayHello(user3)

# 다음과 같이도 사용 가능
# 인스턴스 이름.메서드 이름()
# 인스턴스의 메서드를 호출

user1.SayHello()      # 파라미터를 호출할 필요 없음