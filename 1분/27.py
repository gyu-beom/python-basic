# if 조건문 2

'''
- elif
앞의 조건이 참이 아닌 경우 다른 조건을 다시 한번 확인하기 위한 용도
if와 else 사이에 원하는 만큼 여러 개 넣을 수 있음

if 조건1:
    이 문장
elif 조건2:
    저 문장
else:
    그 문장
다음 문장
'''

today = '토요일'

if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한 잔')
print('공부 시작')

# if 조건이 참이면 elif, else는 실행하지 않음

temp = 40
if temp >= 39:
    print('고열입니다')
elif temp >= 38:
    print('미열입니다')
else:
    print('정상입니다')