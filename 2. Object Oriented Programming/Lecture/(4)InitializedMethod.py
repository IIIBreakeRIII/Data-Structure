class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()                                                # User 생성 줄
user1.initialize("Young", "young@codeit.kr", "123456")        # 초기값 설정하는 줄
    
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

# __init__
# 인스턴스가 생성될 때 자동으로 호출됨

class User:
    def __init__(self, name, email, password):                # Magic Method(Special Method) -> 특수 메서드 : 특정 상황에서 자동으로 호출되는 메서드
        self.name = name
        self.email = email
        self.password = password

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 1. User 인스턴스 생성
# 2. __init__ 메서드 자동 호출

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)