# while

'''
- while
for : 리스트와 같은 반복 대상에서 값을 하나씩 꺼내서 반복 작업 수행
while : 조건이 만족하는 동안 끝없이 반복

while 조건:
  실행 명령문1
  실행 명령문2
  실행 명령문3
'''

customer = '토르'
index = 5

while index >= 1:
  print(f'{customer}, 커피가 준비 되었습니다 {index} 번 남았어요')
  index -= 1
  if index == 0:
    print('커피는 폐기처분되었습니다.')

customer = '토르'
person = 'Unknown'

while person != customer:
  print(f'{customer}, 커피가 준비되었습니다')
  person = input('이름이 어떻게 되세요? ')