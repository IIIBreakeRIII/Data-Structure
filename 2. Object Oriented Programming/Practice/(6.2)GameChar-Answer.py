class GameCharacter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def get_attacked(self, damage):
        if self.is_alive():
            if self.hp >= damage:
                self.hp = self.hp - damage
            else:
                self.hp = 0
        else:
            print("{}은 이미 죽었습니다.".format(self.name))

    def attack(self, other_character):
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        return self.name + "님의 hp는 " + str(self.hp) + "만큼 남았습니다."

character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)