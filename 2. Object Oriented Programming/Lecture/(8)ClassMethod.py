class User:
  count = 0

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password

    User.count += 1

  def SayHello(self):
    print("안녕하세요! 저는 {}입니다.".format(self.name))

  def __str__(self):
    return "사용자: {}, 이메일: {}".format(self.name, self.email)

  @classmethod    # 데코레이터 : NumberOfUsers를 클래스 메서드로 만들어줌
  def NumberOfUsers(cls):           # 클래스 메서드 규칙 1 : 첫번째 파라미터의 이름은 꼭 cls 사용, User Class를 나타냄
    print("총 유저 수 : {}입니다.".format(cls.count))

user1 = User("박제언", "jeeon@email.com", "12345")
user2 = User("류현소", "hyeonso@email.com", "13579")
user3 = User("김연아", "yuna@email.com", "24680")

User.NumberOfUsers()
user1.NumberOfUsers()