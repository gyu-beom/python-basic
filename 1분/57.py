# 메소드 오버라이딩

'''
- 메소드 오버라이딩
부모 클래스의 메소드를 자식 클래스에서 새롭게 정의하는 것

- 메소드 오버라이딩 지식
1. 자식 클래스에서 같은 메소드를 새로 정의하지 않으면 부모 클래스의 메소드 사용
2. 자식 클래스에서 같은 메소드를 새로 정의하면 자식 클래스의 메소드 사용
'''

# 추억용 영상 제작 기능 구현 클래스
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

# 메일 발송 기능 구현 클래스
class MailSender:
    def send(self):
        print('메일 발송')

# 기본 블랙박스
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 여행 모드 지원 블랙박스
class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
    
    def set_travel_mode(self, min):
        print(f'{str(min)} 분 동안 여행 모드 ON')

# (개선) 여행 모드 지원 블랙박스
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(f'{str(min)} 분 동안 여행 모드 ON')
        self.make()
        self.send()

b1 = TravelBlackBox('하양이', 100000, 64)
b1.set_travel_mode(20)

b2 = AdvancedTravelBlackBox('초록이', 120000, 64)
b2.set_travel_mode(15)