# 외장함수

'''
- 외장함수
내장함수와는 다르게 외장함수를 사용하기 위해서는 반드시 해당 모듈을 import 해야 함

https://docs.python.org/3/py-modindex.html

glob : 어떤 경로 내의 폴더 또는 파일의 목록 조회, 윈도우의 dir 명령과 비슷
os : 운영체제에서 제공하는 기본 기능
time : 현재 시간 정보 확인
datetime : time 과 비슷한 모듈, 오늘 날짜 출력
'''

# glob
import glob
print(glob.glob('*.py'))

# os
import os
print(os.getcwd()) # 현재 디렉터리 current working directory

# os - 새로운 폴더 만들기
folder = '11-08-sample_dir'

if os.path.exists(folder): # 폴더가 존재한다면
    print('이미 존재하는 폴더입니다')
    os.rmdir(folder) # 폴더 삭제
    print(f'{folder} 폴더를 삭제하였습니다')
else: # 폴더가 존재하지 않는다면
    os.makedirs(folder) # 폴더 생성
    print(f'{folder} 폴더를 생성하였습니다')

# os listdir() - glob glob() 비슷하며 현재 작업 디렉터리 내의 폴더와 파일 목록 출력
print(os.listdir())

# time
import time

print(time.localtime())

# time strftime()
print(time.strftime('%Y-%m-%d %H:%M:%S'))

# datetime
import datetime

print(f'오늘 날짜는 {datetime.date.today()}')

# datetime timedelta() - 두 날짜 사이의 간격 계산
today = datetime.date.today() # 오늘 날짜 지정
td = datetime.timedelta(days=100) # 100일 저장

print(f'우리가 만난지 100일은 {today + td}')