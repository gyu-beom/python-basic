# 에러

'''
- 에러
ZeroDivisionError : 0으로 나누었을 떄 발생하는 에러
TypeError : 타입이 맞지 않을 때 발생하는 에러
Exception : 일반적인 모든 에러
'''

num1 = 3
num2 = 0

try:
    result = num1 / num2
    print(f'연산 결과는 {result} 입니다')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:
    print(f'에러가 발생했어요 : {err}')