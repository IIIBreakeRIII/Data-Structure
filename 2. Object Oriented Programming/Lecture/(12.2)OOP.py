# 객체 지향 프로그래밍
# 속성과 행동을 갖는 객체들이 행동을 하는 방식으로 작성

class Person:
    
    # 사람을 나타내는 클래스
    def __init__(self, name, age, gender):

        # 사람의 이름, 나이, 성별을 속성으로 갖음
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):

        # 자신의 정보를 출력하는 메서드
        print("사람 한 명을 소개합니다.")
        print("{}님은 {}살이고 {}입니다.".format(self.name, self.age, self.gender))

    def is_underage(self):

        # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 메서드
        return self.age < 20


paul = Person("Paul", 20, "Male")
yuna = Person("Yuna", 18, "Female")

paul.print_info()
yuna.print_info()

print(paul.is_underage())
print(yuna.is_underage())
