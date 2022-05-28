# 퀴즈

'''
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수 구하는 프로그램

조건 1 : 승객별 운행 소요 시간 5분 ~ 50분 사이의 난수
조건 2 : 소요 시간 5분 ~ 15분 사이의 승객만 매칭

출력 예제
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번쨰 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

'''
< 내 풀이 >
from random import *

passenger = list(range(1, 51))
count = 0

for i in passenger:
  time = randint(5, 50)
  if 5 <= time <= 15:
    print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
    count += 1
  else:
    print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')

print(f'총 탑승 승객 : {count} 분')
'''

from random import *

cnt = 0 # 총 탑승 승객 수

for i in range(1, 51):
  time = randrange(5, 51)

  if 5 <= time <= 15:
    print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
    cnt += 1
  else:
    print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')

print(f'총 탑승 승객 : {cnt}분')