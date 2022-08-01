# 다중상속

'''
- 다중상속
여러 클래스로부터 상속을 받음
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

b1 = TravelBlackBox('하양이', 100000, 64)
b1.make()
b1.send()