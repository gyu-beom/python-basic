# if 조건문 1

'''
- if
만약 ~ 라면 이라는 조건을 통해 분기를 태울 수 있음
조건이 참일 때만 수행할 수 있는 문장 구사 가능

if 조건:
    이 문장
다음 문장

- if, else
만약 ~ 라면 if 내의 문장들이 실행
그렇지 않다면 else 내의 문장들이 실행

if 조건:
    이 문장
else:
    저 문장
다음 문장
'''

today = '일요일'

if today == '일요일':
    print('게임 한 판')
print('공부 시작')

today = '일요일'

if today == '일요일':
    print('게임 한 판')
else:
    print('폰 5분만')
print('공부 시작')