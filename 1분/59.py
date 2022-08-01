# 예외처리

'''
- 예외처리
에러를 마주했을 때도 프로그램이 올바로 동작할 수 있도록 해주는 것

- 예외처리 사용법
try:
    에러가 발생할 가능성이 있는 문장
except:
    에러 상황이 발생했을 때만 수행할 문장
else:
    에러가 발생하지 않았을 때만 수행할 문장
finally:
    에러 여부 상관 없이 항상 수행되는 문장

- 예외처리 4가지 방식
1.
try:
    수행 문장
except:
    에러 처리

2.
try:
    수행 문장
finally:
    마지막 수행

3.
try:
    수행 문장
except:
    에러 처리
else:
    정상 동작

4.
try:
    수행 문장
except:
    에러 처리
else:
    정상 동작
finally:
    마지막 수행
'''
num1 = 3
num2 = 2

try:
    result = num1 / num2
    print(f'연산 결과는 {result} 입니다')
except:
    print('에러가 발생했어요')
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')