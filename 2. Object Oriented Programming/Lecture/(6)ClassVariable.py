class User:
  count = 0                                   # User 인스턴스의 총 개수, Class 바로 밑에 정의

  def __init__(self, name, email, pw):

    # 유저 인스턴스의 모든 변수를 지정해주는 메서드
    self.name = name
    self.email = email
    self.pw = pw

    User.count += 1

user1 = User("jeeon", "jeeon@email.com", "12345")
user2 = User("paul", "paul@email.com", "13579")

print(User.count)                           # User 클래스가 실행될 때마다 count값은 1씩 증가

user1.count = 5                             # user1에 count라는 변수가 생기고, 값이 5가 됨 / 즉 같은 이름의 인스턴스 변수가 생성
# 같은 이름의 클래스 변수와 인스턴스 변수는 인스턴스 변수로 인식하게 됨
User.count = 5                              # 다음과 같이 설정해야함

print(user1.count)                          # 이것도 가능
print(user2.count)

