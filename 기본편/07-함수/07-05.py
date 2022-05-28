# 가변인자

'''
- 가변인자
변할 수 있는 인자
서로 다른 개수의 값들을 전달해야 하는 경우

def 함수이름 (전달값1, 전달값2, ..., *가변인자):
  실행 명령문1
  실행 명령문2
  ...
  return 반환값
'''

def profile(name, age, *language):
  print(f'이름 : {name}\t나이 : {age}\t', end=' ')

  for lang in language:
    print(lang, end=' ')
  print()

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript')
profile('김태호', 25, 'Kotlin', 'Swift')