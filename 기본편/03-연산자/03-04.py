# 랜덤함수

'''
a 이상 b 미만의 임의의 값 : random()
a 이상 b 미만의 임의의 정수 값 : randrange()
a 이상 b 이하의 임의의 정수 값 : randint()
'''

from random import *

# random()
print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 이상 10 미만의 임의의 정수 값 생성
print(int(random() * 10) + 1) # 1 이상 11 미만의 임의의 정수 값 생성
print(int(random() * 45) + 1) # 1 이상 46 미만의 임의의 정수 값 생성

# randrange()
print(randrange(1, 46)) # 1 이상 46 미만의 임의의 정수 값 생성

# randint()
print(randint(1, 45)) # 1 이상 45 이하의 임의의 정수 값 생성