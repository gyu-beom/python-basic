# 불리안

'''
형 변환 총 4개
정수로 : int()
실수로 : float()
문자로 : str()
불리안으로 : bool()

bool()
- 값이 있으면 : True
- 값이 없으면 : False
'''

a = 'hello' # 값 있음
b = '     ' # 값 있음
c = '' # 값 없음

print(bool(a)) # True
print(bool(b)) # True
print(bool(c)) # False

a = 1 # 값 있음
b = -2 # 값 있음
c = 0 # 값 없음

print(bool(a)) # True
print(bool(b)) # True
print(bool(c)) # False

# None
print(bool(None)) # False