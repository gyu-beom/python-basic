# with

'''
- with
파일을 열었으면 반드시 닫아주어야 하는데 자주 잊어 먹는 에러사항 발생
with 블럭을 벗어나면 자동으로 파일 닫음

with open(파일명, 열기모드, encoding='인코딩') as 약어:
'''

FILE_PATH = './1분/'

# 파일 쓰기
with open(f'{FILE_PATH}list.txt', 'w', encoding='utf8') as f:
    f.write('김XX\n')
    f.write('정XX\n')
    f.write('허XX\n')

# 파일 읽기
with open(f'{FILE_PATH}list.txt', 'r', encoding='utf8') as f:
    contents = f.read()
    print(contents)