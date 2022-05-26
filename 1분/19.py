# 튜플 2

'''
- 튜플

- 패킹
오른쪽의 값들을 왼쪽의 변수에 묶어서 넣는다

- 언패킹
오른쪽 변수의 값을 왼쪽의 변수"들"에 풀어서 대입한다
특정 부분 모두 풀어서 대입 (리스트) : *
'''

my_tuple = ('오예스', '몽쉘', '초코파이') # 패킹
(pie1, pie2, pie3) = my_tuple # 언패킹

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(one, two, *others) = numbers
'''
one : 1
two : 2
others : [3, 4, 5, 6, 7, 8, 9, 10]
'''

print(one, two, others)

(*others, nine, ten) = numbers
'''
others : [1, 2, 3, 4, 5, 6, 7, 8]
nine : 9
ten : 10
'''

print(others, nine, ten)

(one, *others, ten) = numbers
'''
one : 1
others : [2, 3, 4, 5, 6, 7, 8, 9]
ten : 10
'''

print(one, others, ten)