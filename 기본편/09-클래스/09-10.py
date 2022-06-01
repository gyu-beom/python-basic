# 스타크래프트 프로젝트 전반전

'''
- 스타크래프트 프로젝트 전반전
텍스트 기반의 스타크래프트 프로젝트

- 클래스 변수
클래스 이름과 함께 어디서든지 사용 가능
멤버변수가 각 클래스 객체마다 다른 값을 가진다면 클래스 변수는 모든 객체가 동일한 값을 가짐
'''
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{self.name} 유닛이 생성되었습니다')
    
    def move(self, location):
        print(f'{self.name} : {location} 방향으로 이동합니다 [속도 {self.speed}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]')

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5) # 이름, 체력, 이동속도 공격력
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print(f'{self.name} : 스팀팩을 사용합니다 (HP 10 감소)')
        else:
            print(f'{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다')

# 탱크
class Tank(AttackUnit):
    siege_developed = False # 클래스 변수

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈 모드 (해제 상태)

    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return
        
        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print(f'{self.name} : 시즈모드로 전환합니다')
            self.damage *= 2
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print(f'{self.name} : 시즈모드를 해제합니다')
            self.damage /= 2
            self.siege_mode = False # 시즈 모드 해제

# 날 수 있는 기능을 가진 클래스
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
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5) # 이름, 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)
    
    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print(f'{self.name} : 클로킹 모드 해제합니다')
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print(f'{self.name} : 클로킹 모드 설정합니다')
            self.cloaked = True