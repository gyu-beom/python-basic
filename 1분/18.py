# 튜플 1

'''
- 튜플
수정 불가
읽기 전용 리스트
중복 허용
다양한 자료형
순서 보장
슬라이싱

튜플 = (값1, 값2, ...)

어떤 값이 몇 개 있는지 : count()
어떤 값이 어디에 있는지 : index()
'''

my_tuple = ('오예스', '몽쉘', '초코파이', '초코파이') # 중복 허용
your_tuple = (1, 2, 3.14, True, False, '아무거나') # 다양한 자료형

my_tuple = ('오예스', '몽쉘', '초코파이')

print(my_tuple[0]) # 오예스

# 슬라이싱
print(my_tuple[0:2]) # ('오예스', '몽쉘')

# 포함
print('몽쉘' in my_tuple) # True

# 길이 확인
print(len(my_tuple)) # 3