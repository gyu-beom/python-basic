# 퀴즈

'''
보고서는 항상 아래와 같은 형태로 출력되어야 함

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 생성
'''

FILE_PATH="./기본편/08-입출력/퀴즈/"

for week in range(1, 51):
    with open(f'{FILE_PATH}{week}주차.txt', 'w', encoding='utf8') as week_report:
        week_report.write(f'- {week} 주차 주간보고 -')
        week_report.write('\n부서 : ')
        week_report.write('\n이름 : ')
        week_report.write('\n업무 요약 : ')