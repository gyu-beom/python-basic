# 예외처리

'''
- 예외처리
예상치 못한 어떤 실책이나 실수 또는 잘못된 무언가를 에러 (error) 라고 하며 에러 상황을 처리하는 것

try:
    # 실행하려는 코드
    실행 명령문1
    실행 명령문2
    ...
except 에러종류1:
    # 어떤 에러에 대한 처리를 하는 코드
    예외 처리 명령문1
    예외 처리 명령문2
    ...
except 에러종류2:
    예외 처리 명령문1
    예외 처리 명령문2
    ...

값이 잘못되어서 발생하는 에러 : ValueError
0으로 나누어서 발생하는 에러 : ZeroDivisionError
지금까지 정의되지 않은 모든 에러 : Exception
'''

try:
    print('나누기 전용 계산기입니다')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번쨰 숫자를 입력하세요 : ')))
    nums.append(int(nums[0] / nums[1]))
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다')
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print('알 수 없는 에러가 발생하였습니다')
    print(err)