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

  # NumberOfUsers는 인스턴스 변수를 사용하지 않기 때문
  # self 파라미터 사용 안함
  def NumberOfUsers(self):
    print("총 유저 수는 : {}입니다.".format(User.count))

user1 = User("박제언", "jeeon@email.com", "12345")
user2 = User("류현소", "hyeonso@email.com", "13579")
user3 = User("김연아", "yuna@email.com", "24680")

# 클래스 메서드 사용
User.NumberOfUsers(user1)
user1.NumberOfUsers()
