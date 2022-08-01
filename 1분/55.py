# super

'''
- super
super() 를 통해서 부모 클래스의 정보를 가져올 수 있음

- super 사용
super().메소드()

- super 사용 시 주의사항
1. () 괄호를 꼭 사용해야 함
2. 메소드 기입 시 self 는 기재하지 않음
'''

# 기본 블랙박스
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 여행 모드 지원 블랙박스
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        # BlackBox.__init__(self, name, price)
        super().__init__(name, price)
        self.sd = sd
    
    def set_travel_mode(self, min):
        print(f'{str(min)} 분 동안 여행 모드 ON')