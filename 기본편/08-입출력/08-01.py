# 표준입출력

'''
- 표준입출력
분리 기호 : sep()
개행 기호 : end()

- 표준 출력 및 표준 에러
import sys
file=sys.stdout # 표준 출력
file=sys.stderr  # 표준 에러
: 큰 규모의 파이썬 프로젝트를 진행하면 stdout, stderr의 사용 용도가 달라짐
- 일반적인 결과 정보의 내용을 로그로 남김 : stdout()
- 에러 발생 시 관련 내용을 출력하기 위함 : stderr()

- 자리 채움
* 적용 대상이 문자열이어야 함
전달하는 숫자값 만큼 미리 공간 확보 (글이 왼쪽에 채워짐) : ljust()
전달하는 숫자값 만큼 미리 공간 확보 (글이 오른쪽에 채워짐) : rjust()
전달하는 숫자값 만큼 미리 공간 확보 후 그 공간을 zero (0) 으로 채움 zfill()

- 표준 입력
입력 : input()
'''

# 분리 기호 sep()
print('Python', 'Java', sep=',') # Python,Java
print('Python', 'Java', sep=', ') # Python, Java
print('Python', 'Java', 'JavaScript', sep=', ') # Python, Java, JavaScript

# 개행 기호 end()
print('Python', 'Java', end='?')

# 표준 출력 및 표준 에러
import sys
print('Python', 'Java', file=sys.stdout) # 표준 출력
print('Python', 'Java', file=sys.stderr) # 표준 에러

# 자리 채움 ljust(), rjust()
scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')

# 자리 채움 zfill()
for num in range(1, 21):
    print(f'대기번호 : {str(num).zfill(3)}')

# 표준 입력 input()
answer = input('아무 값이나 입력해주세요 : ')
print(f'{answer} {type(answer)}') # 모든 값이 문자열