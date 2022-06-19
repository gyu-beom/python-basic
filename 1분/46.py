# 파일입출력

'''
- 파일입출력
open(파일명, 열기모드, encoding='인코딩')

- 열기모드
r : read (읽기)
a : append (이어서 쓰기)
w : write (쓰기)

- 파일은 열었으면 반드시 닫아주어야 함
close()
'''

FILE_PATH='./1분/'

# 파일 쓰기
f = open(f'{FILE_PATH}list.txt', 'w', encoding='utf8') # 쓰기 모드로 파일 쓰기
f.write('김XX\n') # 문장 입력
f.write('정XX\n') # 문장 입력
f.write('허XX\n') # 문장 입력
f.close() # 파일 닫기

# 읽기 모드로 파일 열기
f = open(f'{FILE_PATH}list.txt', 'r', encoding='utf8') # 읽기 모드로 파일 열기
contents = f.read() # 파일 내용 다 읽어오기
print(contents)
f.close() # 파일 닫기

# 읽기 모드로 파일 열기
f = open(f'{FILE_PATH}list.txt', 'r', encoding='utf8') # 읽기 모드로 파일 열기
for line in f:
    print(line, end='')
f.close() # 파일 닫기