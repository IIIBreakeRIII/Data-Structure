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