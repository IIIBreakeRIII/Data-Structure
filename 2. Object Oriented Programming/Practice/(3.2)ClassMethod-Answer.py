class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):

        # 각 변수에 분리된 문자열 저장
        param_list = string_params.split(",")

        name = param_list[0]
        email = param_list[1]
        password = param_list[2]
        
        # 인스턴스 생성 후 리턴
        return cls(name, email, password)

    @classmethod
    def from_list(cls, list_param):
        name = list_param[0]
        email = list_param[1]
        password = list_param[2]

        # 인스턴스 생성 후 리턴
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])
    
print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
