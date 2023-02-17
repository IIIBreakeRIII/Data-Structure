class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def SayHello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))

user1 = User("Paul", "paul@email.com", "123456")

print(type(user1))                                                  # <class '__main__.User'>

print(type(2))                      # 정수                          # <class 'int'>
print(type("string"))               # 문자열                        # <class 'str'>
print(type([]))                     # 리스트                        # <class 'list'>
print(type({}))                     # 딕셔너리                      # <class 'dict'>
print(type(()))                     # 튜플                          # <class 'tuple'>

def PrintHello():
    print('안녕하세요!!')

print(type(PrintHello))             # 함수                          # <class 'function'>

# 위의 클래스들은 모두 기존에 만들어진 내장된 클래스들
# 기본적으로 파이썬에서 제공하는 클래스들 -> 즉, 파이썬은 순수 객체 지향 언어들

IntList = []

IntList.append(1)
IntList.append(3)
IntList.append(7)

print(IntList)
