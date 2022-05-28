# for

'''
- for
분기만큼 중요한 것이 반복
'''

for waiting_no in [0, 1, 2, 3, 4]:
  print(f'대기번호 : {waiting_no}')

for waiting_no in range(5):
  print(f'대기번호 : {waiting_no}')

for waiting_no in range(1, 6):
  print(f'대기번호 : {waiting_no}')

starbucks = ['아이언맨', '토르', '아이엠 그루트']
for custom in starbucks:
  print(f'{custom}, 커피가 준비되었습니다')