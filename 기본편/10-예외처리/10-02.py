# 에러 발생시키기

'''
- 에러 발생시키기
실제로 에러 상황이 발생한 것이 아니더라도 프로그램이 허용하지 않는 동작을 하려고 할 때 의도적으로 에러를 발생시킬 수 있음

raise 에러종류
'''

try:
    print('한 자리 숫자 나누기 전용 계산기입니다')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번쨰 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError
    print(f'{num1} / {num2} = {int(num1 / num2)}')
except ValueError:
    print('잘못된 값을 입력하였습니다 | 한 자리 숫자만 입력하세요')