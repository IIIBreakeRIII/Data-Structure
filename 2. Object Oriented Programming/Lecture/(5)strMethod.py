class User:
  def __init__(self, name, email, pw):
    self.name = name
    self.email = email
    self.pw = pw
  
  def SayHello(self):
    print("안녕하세요! 저는 {}입니다.".format(self.name))

  # __str__ : print 함수를 호출할 때 자동으로 호출

  def __str__(self):        #Double Underscore Method -> Dunder Method
    return "사용자: {}, 이메일: {}, 비밀번호: *****".format(self.name, self.email)

user1 = User("jeeon", "jeeon@email.com", "12345")
user2 = User("paul", "paul@email.com", "13579")

print(user1)
print(user2)