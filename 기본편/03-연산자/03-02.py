# 간단한 수식

# 연산자 우선순위
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14

number += 2 # number = number + 2
print(number) # 16

number *= 2 # number = number * 2
print(number) # 32

number //= 2 # number = number // 2
print(number) # 16

number /= 2 # number = number / 2
print(number) # 8.0

'''
파이썬은 기본적으로 나눗셈 연산 시, 소수로 출력
소수점을 없애고 싶은 경우
number /= 2
number = int(number)
print(number)
'''

number -= 2 # number = number - 2
print(number) # 6.0

number %= 2 # number = number % 2
print(number) # 0.0