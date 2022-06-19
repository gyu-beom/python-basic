# 사용자입력

'''
- 사용자입력
input()

input()으로 입력 받은 모든 입력값은 문자열
'''

name = input('예약자분 성함이 어떻게 되나요? ')
print(name)

num = int(input('총 몇 분이세요? '))
if num > 4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다.')