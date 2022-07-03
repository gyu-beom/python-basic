# 메소드

'''
- 클래스
여러 개의 변수를 가질 수 있지만 여러 개의 기능을 하는 함수 또한 가질 수 있음.

- __init__
객체가 생성될 떄 자동으로 실행되는 함수.

- 메소드
__init__() 과 같이 클래스 내에 선언된 함수를 메소드라고 함.
'''

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min):
        print(f'{str(min)}분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(20)