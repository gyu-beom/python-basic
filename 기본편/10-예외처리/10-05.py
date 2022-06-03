# 퀴즈

'''
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템 제작
시스템 코드를 확인하고 적절한 예외처리 구문 작성

조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
    - 출력 메세지 : "잘못된 값을 입력하였습니다"
조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
    - 치킨 소진 시 사용자 정의 에러 [SoldOutError] 를 발생시키고 프로그램 종료
    - 출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다"

코드
chicken = 10 # 남은 치킨 수
waiting = 1 #  홀 안에는 현재 만석. 대기번호 1부터 시작

while(True):
    print(f'[남은 치킨] : {chicken}')
    order = int(input('치킨 몇 마리 주문하시겠습니까?'))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print('재료가 부족합니다')
    else:
        print(f'[대기 번호 {waiting}] {order} 마리 주문이 완료되었습니다')
        waiting += 1 # 대기번호 증가
        chicken -= order # 주문 수 만큼 남은 치킨 감소
'''

'''
< 내 풀이>
class SoldOutError(Exception):
    def __init__(self):
        pass

chicken = 10
waiting = 1

try:
    while(True):
        print(f'[남은 치킨] : {chicken}')
        order = int(input('치킨 몇 마리 주문하시겠습니까? '))
        # ValueError
        if order < 1:
            raise ValueError
        # Main
        if order > chicken:
            print('재료가 부족합니다')
        else:
            print(f'[대기 번호 {waiting}] {order} 마리 주문이 완료되었습니다')
            waiting += 1
            chicken -= order
        # SoldOutError
        if chicken == 0:
            raise SoldOutError
except ValueError:
    print('잘못된 값을 입력하였습니다')
except SoldOutError:
    print('재고가 소진되어 더 이상 주문을 받지 않습니다')
'''

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        print(f'[남은 치킨] : {chicken}')
        order = int(input('치킨 몇 마리 주문하시겠습니까? '))
        if order > chicken:
            print('재료가 부족합니다')
        # ValueError
        elif order <= 0:
            raise ValueError
        else:
            print(f'[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다')
            waiting += 1
            chicken -= order
        # SoldOutError
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다')
    except SoldOutError:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다')
        break