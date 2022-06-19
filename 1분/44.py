# 전역변수

'''
- 전역변수
함수 안이나 밖이나 상관없이 어디서든 사용할 수 있음
함수 밖에서 정의한 변수는 모두 전역변수

만일, 함수 내에서 동일한 변수명이 있다면 해당 지역변수가 우선적으로 작용
만일, 함수 내에서 전역 변수를 사용하여 값 변경을 원한다면 global 키워드 사용
'''

message = '나는야 전역 변수'

print(message) # 나는야 전역 변수

def no_secret():
    message = '이러면 또 지역 변수'
    print(message) # 이러면 또 지역 변수

no_secret()

def no_secret():
    global message
    message = '오 진짜 전역 변수!!'
    print(message)

no_secret()

print(message)