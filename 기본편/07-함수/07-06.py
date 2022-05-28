# 지역변수와 전역변수

'''
- 지역변수와 전역변수

전역변수를 많이 쓰게 되면 코드 관리가 어려워짐, 가급적 사용하지 않는 편이 좋음
'''

# 전역변수
from tabnanny import check


gun = 10

def checkpoint(soldiers):
  global gun
  gun = gun - soldiers
  print(f'[함수 내] 남은 총 : {gun}')

print(f'전체 총 : {gun}')
checkpoint(2)
print(f'남은 총 : {gun}')

# 지역변수
gun = 10

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print(f'[함수 내] 남은 총 : {gun}')
  return gun

print(f'전체 총 : {gun}')
gun = checkpoint_ret(gun, 2)
print(f'남은 총 : {gun}')