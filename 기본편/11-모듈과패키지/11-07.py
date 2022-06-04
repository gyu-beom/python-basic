# 내장함수

'''
- 내장함수 (built-in function)
별도로 import 를 하지 않고도 사용할 수 있도록 내장되어 있는 함수

- dir()
어떤 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 목적으로 사용
만약 전달값으로 아무것도 넘기지 않는다면 현재 소스코드 범위 내에서 사용 가능한 모듈 또는 객체 출력
'''

print(dir()) # 현재 사용 가능한 내장함수 출력

import random
print(dir()) # 현재 사용 가능한 내장함수 + random 출력

import pickle
print(dir()) # 현재 사용 가능한 내장함수 + pickle 출력

print(dir(random)) # random 에서 사용 가능한 함수 출력

lst = [1, 2, 3]
print(dir(lst)) # list 에서 사용 가능한 함수 출력

name = 'Jim'
print(dir(name)) # 문자열 에서 사용 가능한 함수 출력