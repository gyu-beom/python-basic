# 상속

'''
- 상속
공통되는 부분은 코드를 중복으로 적지 않고도 재사용을 할 수 있음

class 자식클래스(상속받을 부모클래스):
'''

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage

    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다')

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)