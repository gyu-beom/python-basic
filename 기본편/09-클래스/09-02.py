# __init__

'''
- __init__
생성자 (Constructor) : 사용자가 따로 호출하지 않아도 클래스 객체를 생성할 때 자동으로 호출이 되는 부분
* 단, 객체를 생성할 때 이 생성자의 전달값에 해당하는 갯수만큼 값을 던져줘야 함. (self 부분 제외)
'''

class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다')
        print(f'체력 {self.hp}, 공격력 {self.damage}')

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)

# 에러
# marine3 = Unit('마린') # 전달값 2개 필요하다는 에러 뜸
# marine3 = Unit('마린', 40) # 전달값 1개 필요하다는 에러 뜸