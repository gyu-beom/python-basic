# 멤버변수

'''
- 멤버변수
클래스 내에서 정의된 변수
self. 와 함께 사용할 수 있음

- 변수 접근 방법
클래스 내 : self. 으로 멤버변수에 접근
객체 내 : 객체이름.멤버변수
'''

class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')

wraith1 = Unit('레이스', 80, 5)
print(f'유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}')

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('빼앗은 레이스', 80, 5)
# 빼앗은 레이스에 cloaking 기능 있다고 가정
wraith2.cloaking = True
if wraith2.cloaking == True:
    print(f'{wraith2.name}는 현재 클로킹 상태입니다')

# if wraith1.cloaking == True:
#    print(f'{wraith1.name}는 현재 클로킹 상태입니다') # 에러 발생
