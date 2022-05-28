# if

'''
- if
조건에 따라 동작이 달라지는 것 : 분기

if 조건:
  실행 명령문

if 조건1:
  실행 명령문1
elif 조건2:
  실행 명령문2
elif 조건3:
  실행 명령문3
else:
  실행 명령문4
'''

weather = '비'

if weather == '비':
  print('우산을 챙기세요')

weather = '미세먼지'

if weather == '비':
  print('우산을 챙기세요')
elif weather == '미세먼지':
  print('마스크를 챙기세요')

weather = '맑아요'

if weather == '비':
  print('우산을 챙기세요')
elif weather == '미세먼지':
  print('마스크를 챙기세요')
else:
  print('준비물 필요 없어요')

weather = input('오늘 날씨는 어때요? ')

if weather == '비' or weather == '눈':
  print('우산을 챙기세요')
elif weather == '미세먼지':
  print('마스크를 챙기세요')
else:
  print('준비물 필요 없어요')

temp = int(input('기온은 어때요? '))

if 30 <= temp:
  print('너무 더워요 나가지 마세요')
elif 10 <= temp < 30: # elif 10 <= temp and temp < 30:
  print('괜찮은 날씨에요')
elif 0 <= temp < 10: # elif 0 <= temp and temp < 10:
  print('외투를 챙기세요')
else:
  print('너무 추워요 나가지 마세요')