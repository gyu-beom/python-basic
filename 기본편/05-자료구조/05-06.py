# 퀴즈

'''
댓글 이벤트 진행
댓글 작성자 중 추첨을 통해 1명 치킨, 3명 커피 쿠폰

조건 1 : 편의상 댓글은 20명 작성, 아이디는 1 - 20 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample 활용

출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --
'''

'''
shuffle, sample 예제

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
'''

'''
< 내 풀이 >
from random import *

comment = [i for i in range(1, 21)]
shuffle(comment)
winner = sample(comment, 4)
chicken_winner = winner[0]
coffee_winners = winner[1:]

print('-- 당첨자 발표 --')
print(f'치킨 당첨자 : {chicken_winner}')
print(f'커피 당첨자 : {coffee_winners}')
print('-- 축하합니다 --')
'''

'''
< 나도코딩 - 1 : 리스트 >
from random import *

users = list(range(1, 21))
shuffle(users)
winners = sample(users, 4)
print('-- 당첨자 발표 --')
print(f'치킨 당첨자 : {winners[0]}')
print(f'커피 당첨자 : {winners[1:]}')
print('-- 축하합니다 --')
'''

'''
< 나도코딩 - 2 : 세트 >
'''

from random import *

users = list(range(1, 21))
shuffle(users)
chicken_winner = sample(users, 1)
remain_users = set(users) - set(chicken_winner)
coffee_winners = sample(remain_users, 3)

print('-- 당첨자 발표 --')
print(f'치킨 당첨자 : {chicken_winner}')
print(f'커피 당첨자 : {coffee_winners}')
print('-- 축하합니다 --')