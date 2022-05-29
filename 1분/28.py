# if 중첩

'''
- if 중첩
if 문 내에서 또 다른 if 문을 사용하는 경우

if 조건1:
    이 문장
    if 조건2:
        저 문장
다음 문장
'''

yellow_card = 0
foul = True

if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴... 조심해야지')
else:
    print('주의')
