# 숫자처리함수

'''
- 기본적으로 제공하는 숫자 처리 함수
절대값 : abs
제곱 : pow
가장 큰 값 : max
가장 작은 값 : min
반올림 : round

- math 모듈에서 제공하는 숫자 처리 함수
내림 : floor
올림 : ceil
제곱근 : sqrt
'''

# 기본적으로 제공하는 숫자 처리 함수
print(abs(-5)) # 5
print(pow(4, 2)) # 16 (4 ** 2)
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

# math 모듈에서 제공하는 숫자 처리 함수
from math import *
print(floor(4.99)) # 4
print(ceil(3.14)) # 4
print(sqrt(16)) # 4.0