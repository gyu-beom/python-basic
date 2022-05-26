# 리스트 2

'''
- 리스트
여러 개의 값을 저장
일반적으로 서로 관련 있는 연속적인 데이터들을 관리하는데 사용
중복 허용
순서 보장
슬라이싱

원하는 위치에 값 추가 : insert()
원하는 위치 (또는 마지막) 의 값 삭제 : pop()
모든 값 삭제 : clear()
값 순서대로 정렬 : sort()
순서 뒤집기 : reverse()
리스트 복사 : copy()
어떤 값이 몇 개 있는지 : count()
어떤 겂이 어디에 있는지 : index()
'''

my_list = ['오예스', '몽쉘', '초코파이']

print(my_list[0]) # 오예스

# 슬라이싱
print(my_list[0:2]) # ['오예스', '몽쉘']

# 포함
print('몽쉘' in my_list) # True

# 길이 확인
print(len(my_list)) # 3

# 리스트 수정 : 값 수정
my_list[1] = '몽쉘카카오' # 값 수정
print(my_list) # ['오예스', '몽쉘카카오', '초코파이']

# 리스트 수정 : 값 추가
my_list.append('빅파이') # 값 추가
print(my_list) # ['오예스', '몽쉘카카오', '초코파이', '빅파이']

# 리스트 수정 : 값 제거
my_list.remove('오예스') # 값 제거
print(my_list) # ['몽쉘카카오', '초코파이', '빅파이']

my_list = ['오예스', '몽쉘', '초코파이']
your_list = ['빅파이', '오뜨']

# 리스트 더하기
my_list.extend(your_list) # 리스트 확장
print(my_list) # ['오예스', '몽쉘', '초코파이', '빅파이', '오뜨']