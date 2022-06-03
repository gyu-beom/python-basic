# 사용자 정의 예외처리

'''
- 사용자 정의 예외처리

ex) BigNumberError
- 어떤 값들이 입력되었는지를 문자열 형태로 작성
- __init__() 생성자의 msg 로 들어감
- except 구문에서는 as 를 이용하여 err 라는 이름으로 에러를 받고 이를 print() 를 통해 출력하면 __str__() 메소드에 의해 반환되는 msg 멤버변수 출력
'''

class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "[에러코드 001]" + self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기입니다')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError(f'입력값 : {num1}, {num2}') # 자세한 에러 메시지
    print(f'{num1} / {num2} = {int(num1 / num2)}')
except ValueError:
    print('잘못된 값을 입력하였습니다 | 한 자리 숫자만 입력하세요')
except BigNumberError as err: # 사용자 정의 에러
    print('에러가 발생하였습니다 | 한 자리 숫자만 입력하세요')
    print(err)