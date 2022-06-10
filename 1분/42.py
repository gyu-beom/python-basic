# 가변인자

'''
- 가변인자
개수가 바뀔 수 있는 인자 (튜플 형태로 값을 받음)
함수를 호출할 때 전달값이 몇 개가 될지 모르는 경우에 개수를 신경 쓸 필요 없이 함수를 쓸 수 있게 해줌

def 함수명(*전달값):
    수행할 문장
'''

def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2022년 6월 10일', '나장발') # 1명 방문
visit('2022년 6월 10일', '나장발', '나수염') # 2명 방문
visit('2022년 6월 10일', '나장발', '나수염', '나김리') # 3명 방문