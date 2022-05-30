# for 활용

'''
- for 반복문
for 변수 in 반복 범위 또는 대상:
    반복 수행 문장

- 반복 대상
리스트, 튜플, 딕셔너리, 문자열
'''

# 리스트
my_list = [1, 2, 3]
for x in my_list:
    print(x)

# 튜플
my_tuple = (1, 2, 3)
for x in my_tuple:
    print(x)

# 딕셔너리
person = {'이름': '나귀욤', '나이': 7, '키': 120, '몸무게': 23}
# 딕셔너리 값
for v in person.values():
    print(v)
# 딕셔너리 키
for k in person.keys():
    print(k)
# 딕셔너리 키, 값
for k, v in person.items():
    print(k, v)

# 문자열
fruit = 'apple'
for x in fruit:
    print(x)