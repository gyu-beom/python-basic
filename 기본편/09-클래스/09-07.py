# 메소드 오버라이딩

'''
- 메소드 오버라이딩 (method overriding)
상속 관계에 있는 클래스들 사이에서 부모 클래스에 정의된 메소드를 그대로 사용하지 않고 자식 클래스에서 같은 이름으로 메소드를 새롭게 정의하여 사용하도록 할 수 있음
'''

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 유닛 속도
    
    def move(self, location): # 이동 함수 정의
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
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # Unit 클래스의 move() 메소드를 새롭게 정의 (오버라이딩)
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 10, 20) # 지상 speed 10

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)


vulture.move('11시')
# battlecruiser.fly(battlecruiser.name, '9시') # 매번 지상 유닛 = move(), 공중 유닛 = fly() 로 하기 번거로움
battlecruiser.move('9시')