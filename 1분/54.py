# 상속

'''
- 상속
어떤 클래스에서 사용한 모든 코드를 그대로 물려받아서 사용하고 거기에다가 추가로 필요한 내용을 확장하는 개념으로 쓸 수 있음
'''

'''
- 상속 사용하지 않을 시
# 기본 블랙박스
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 여행 모드 지원 블랙박스
class TravelBlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min):
        print(f'{str(min)} 분 동안 여행 모드 ON')
'''

# 상속 사용 시
# 기본 블랙박스 (부모 클래스)
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 여행 모드 지원 블랙박스 (자식 클래스)
class TravelBlackBox(BlackBox):
    def set_travel_mode(self, min):
        print(f'{str(min)} 분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 100000)

b2.set_travel_mode(10)