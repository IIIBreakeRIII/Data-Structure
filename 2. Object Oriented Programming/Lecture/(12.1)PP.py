# 절차 지향 프로그래밍
# 반복적으로 사용하는 코드를 함수로 정의

def print_person_info(person_name, person_age, person_gender):

    # 사람의 이름, 나이, 성별을 파라미터로 받으면 받은 정보를 이해할 수 있는 문자열로 출력
    print("사람 한 명을 소개합니다.")
    print("{}님은 {}살이고 {}입니다.".format(person_name, person_age, person_gender))

def is_underage(person_age):

    # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 함수
    return person_age < 20

paul_name = "Paul"
paul_age = 20
paul_gender = "Male"

yuna_name = "Yuna"
yuna_age = 18
yuna_gender = "Female"

print_person_info(paul_name, paul_age, paul_gender)
print_person_info(yuna_name, yuna_age, yuna_gender)

print(is_underage(paul_age))
print(is_underage(yuna_age))
