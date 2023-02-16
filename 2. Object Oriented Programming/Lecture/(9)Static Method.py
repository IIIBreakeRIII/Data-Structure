class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def SayHello(self):
        print("안녕하세요, 저는 {}입니다.".format(self.name))


    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)
    
    @classmethod
    def NumberOfUsers(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

    @staticmethod
    def IsValidEmail(email_address):            # 정적 메서드
        return "@" in email_address


print(User.IsValidEmail("HyeonsoRyu"))
print(User.IsValidEmail("HyeonsoRyu@email.com"))
