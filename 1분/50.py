# __init__

'''
- __init__
클래스 설계도 작성하기.
객체가 생성될 때 자동으로 실행.

class 클래스명:
    def __init__(self, 필요한 변수):
        필요한 변수 정의
'''

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)

b2 = BlackBox('하양이', 100000)
print(b2.name, b2.price)