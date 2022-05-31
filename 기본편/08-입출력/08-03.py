# 파일입출력

'''
- 파일입출력

프로그래밍에서 파일을 다룰 때의 순서
1. 파일을 열고
2. 파일에 어떤 내용을 쓰거나 읽고
3. 파일을 닫는

open('파일명', '열기모드', encoding='인코딩')

- 열기모드
읽기 : r (read)
쓰기 : w (write) -> 이미 생성된 파일에 w 모드이면 기존의 내용 덮어씀
이어쓰기 : a (append)

- 읽기모드
한 줄 읽고 커서는 다음으로 보냄 : readline()
모든 줄을 읽어와서 list 형태로 저장 : readines()
'''

# 쓰기 모드
score_file = open('./기본편/08-입출력/score.txt', 'w', encoding='utf8')
print('수학 : 0', file=score_file) # score.txt 파일에 내용 쓰기
print('영어 : 50', file=score_file) # score.txt 파일에 내용 쓰기
score_file.close()

# 이어쓰기 모드
score_file = open('./기본편/08-입출력/score.txt', 'a', encoding='utf8')
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100') # write()는 줄바꿈 안 해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close()

# 읽기 모드 readline()
score_file = open('./기본편/08-입출력/score.txt', 'r', encoding='utf8')
print(score_file.readline(), end='') # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end='') # 줄바꿈 중복을 방지하기 위해 end='' 처리
print(score_file.readline(), end='')
print(score_file.readline(), end='')
score_file.close()

print() # 예제 때문에 개행

# 읽기 모드 readline() for 활용
score_file = open('./기본편/08-입출력/score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽을 내용이 없다면
        break # 반복문 탈출
    print(line, end='')
score_file.close()

print() # 예제 때문에 개행

# 읽기 모드 reaadlines()
score_file = open('./기본편/08-입출력/score.txt', 'r', encoding='utf8')
lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end='')
score_file.close()