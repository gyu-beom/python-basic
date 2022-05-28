# continue and break

'''
- continue
더 이상 아래 명령들을 실행하지 않고 다음 반복대상으로 넘어갈 떄 사용

- break
즉시 반복문 탈출
'''

absent = [2, 5]

for student in range(1, 11):
  if student in absent:
    continue
  print(f'{student}, 책을 읽어봐')

absent = [2, 5]
no_book = [7]

for student in range(1, 11):
  if student in absent:
    continue
  elif student in no_book:
    print(f'오늘 수업은 여기까지, {student}는 교무실로 따라와')
    break
  print(f'{student}, 책을 읽어봐')