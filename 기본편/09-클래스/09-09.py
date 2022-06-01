# super

'''
- super
부모 클래스의 이름을 직접 찾지 않고도 부모 클래스에 접근하는 방법
* 단, super() 를 사용할 때는 self 를 제외해야 함

다중 상속의 경우 모든 부모 클래스를 명시해야 함
'''
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print('[지상 유닛 이동]')
        print(f'{self.name} : {location} 방향으로 이동합니다 [속도 {self.speed}]')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다')

# 공중 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아갑니다 [속도 {self.flying_speed}]')

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # 부모 클래스 접근, self 없이 사용
        self.location = location

# 다중상속의 경우 super 사용법 : 모두 명시
class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit1(Unit, Flyable):
    def __init__(self):
        super().__init__()

class FlyableUnit2(Flyable, Unit):
    def __init__(self):
        super().__init__()

class FlyableUnit3(Flyable, Unit):
    def __init__(self):
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출

# 드랍쉽
dropship1 = FlyableUnit1() # Unit 생성자 출력
print() # 구분을 위한 개행
dropship2 = FlyableUnit2() # Flyable 생성자 출력
print() # 구분을 위한 개행
dropship3 = FlyableUnit3() # Unit 생성자 출력, Flyable 생성자 출력