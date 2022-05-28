# 자료구조의 변경

'''
- 자료구조의 변경
리스트, 튜플, 세트 간 자유롭게 변환 가능

자료구조의 이름()
'''

menu = {'커피', '우유', '주스'}
print(menu, type(menu))

# 리스트 변환
menu = list(menu)
print(menu, type(menu))

# 튜플 변환
menu = tuple(menu)
print(menu, type(menu))

# 세트 변환
menu = set(menu)
print(menu, type(menu))