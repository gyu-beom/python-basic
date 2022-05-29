# 세트 2

'''
- 세트
순서 보장 X
중복 보장 X

순서 보장 X 때문에 리스트, 튜플처럼 인덱스 접근 불가

값 추가 : add()
값 제거 : remove()
모든 값 제거 : clear()
모든 값, 세트 제거 : del()
세트 복사 : copy()
값 삭제 (해당 값이 없어도 에러 발생 X) : discard()
두 세트에 겹치는 값이 없는지 여부 : isdisjoint()
다른 세트의 부분집합인지 여부 : issubset()
다른 세트의 상위 집합인지 여부 : issuperset()
다른 세트의 값들을 더함 : update()
'''

my_set = {'돈가스', ' 보쌈', '제육덮밥'}

# 값 추가 : add()
my_set.add('닭갈비')
print(my_set)

# 값 제거 : remove()
my_set.remove('제육덮밥')
print(my_set)

# 모든 값 제거 : clear()
my_set.clear()
print(my_set)

# 완전 삭제 : del()
my_set = {'돈가스', '보쌈', '제육덮밥'}
del my_set
# print(my_set) # 에러 발생