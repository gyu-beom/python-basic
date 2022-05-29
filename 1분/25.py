# 자료형 변환

# 튜플에서 값 변경하기
my_tuple = ('오예스', '몽쉘')
my_list = list(my_tuple)
my_list.append('초코파이')
my_tuple = tuple(my_list)
print(my_tuple)

# 리스트에서 중복 제거하기 (순서 보장 X)
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_set = set(my_list)
my_list = list(my_set)
print(my_list)

# 리스트에서 중복 제거하고 순서 보장하기
my_list = ['오예스', '몽쉘', '초코파이', '초코파이', '초코파이']
my_dic = dict.fromkeys(my_list)
print(my_dic)
my_list = list(my_dic)
print(my_list)