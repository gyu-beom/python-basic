# 클래스

'''
- 클래스
하나의 틀, 서로 연관이 있는 변수 (멤버변수) 와 함수 (메소드) 의 집합으로 이루어짐
메소드의 첫 번째 전달값 위치에는 self 적어주어야 함

class 클래스명:
    def 메소드1(self, 전달값1, 전달값2, ...):
        실행명령문1
        실행명령문2
        ...
    
    def 메소드2(self, 전달값1, 전달값2, ...):
        실행명령문1
        실행명령문2
        ...

__init__() 메소드 : 기본적으로 필요한 전달값들을 전달받고 self. 을 통해 클래스의 멤버 변수를 정의
self.변수명 = 값 : 멤버변수
멤버변수 : 클래스 내에서 사용할 수 있는 변수

객체 (Object) : 클래스를 통해서 만들어지는 것
인스턴스 (Instance) : 클래스를 통해 만들어진 객체

변수명 = 클래스명(전달값1, 전달값2, ...) # 전달값은 클래스의 __init__() 에 정의된 부분 중 self 를 제외한 값
'''

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수 name 에 전달값 name 저장
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')

marine1 = Unit('마린', 40, 5) # 마린1 생성, 전달값으로 name, hp, damage 전달
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)