# 내가 제출한 답

class User:
    def initialize(self, name, email, password):
        print(name, email, password)

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
User.initialize(user3, "Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
User.initialize(user4, "Lisa", "lisa@codeit.kr", "abc123")

# 코드잇에서 제공하는 모범 답안

class user:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")
    
user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
    
user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")
    
user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)