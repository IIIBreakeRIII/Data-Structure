class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")
        print(parameter_list[0], parameter_list[1], parameter_list[2])

    @classmethod
    def from_list(cls, list_params):
        print(list_params[0], list_params[1], list_params[2])
        
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])
