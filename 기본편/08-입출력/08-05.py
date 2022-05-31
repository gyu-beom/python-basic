# with

'''
- with
파일을 열고 나서 close() 를 호출하지 않아도 자동으로 닫아주는 역할

with 작업 as 변수명:
    실행 명령문1
    실행 명령문2
    ...
'''

import pickle

FILE_PATH = './기본편/08-입출력/' # 현재 디렉터리 경로 저장 변수 생성

# with pickle 읽기
with open(f'{FILE_PATH}profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))

# with 쓰기
with open(f'{FILE_PATH}study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

# with 읽기
with open(f'{FILE_PATH}study.txt', 'r', encoding='utf8') as study_file:
    lines = study_file.readlines()
    for line in lines:
        print(line, end='')