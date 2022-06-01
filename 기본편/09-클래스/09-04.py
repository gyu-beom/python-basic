# 메소드

'''
- 메소드
클래스에는 여러 개의 메소드를 정의할 수 있음
일반 함수와 다른 점이라면 메소드는 전달값을 정의하는 부분 처음에 self 를 적음
메소드 내에서 self. 을 통해 클래스 멤버변수에 접근 가능함
'''

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    # 유닛 이름과 공격력은 이미 클래스 객체의 멤버 변수로 정의되어 있기 때문에 self. 사용
    # 공격 방향은 명령을 받을 때마다 달라질 수 있으므로 멤버 변수가 아닌 전달값 사용하기 위해 self. 사용 X
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격합니다 [공격력 {self.damage}]')
    
    # 피해 데미지도 상황과 유닛에 따라 달라지므로 변수가 아닌 전달값으로 사용하기 위해 self. 사용 X
    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다')

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃', 50, 15)
firebat1.attack('5시')

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)