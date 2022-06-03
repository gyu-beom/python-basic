# 파일 만들기

file_path = './기본편/10-예외처리/'
file_list = ['01', '02', '03', '04', '05']
file_header = ['# 예외처리', '# 에러 발생시키기', '# 사용자 정의 예외처리', '# finally', '# 퀴즈']

for idx in range(len(file_list)):
    with open(f'{file_path}10-{file_list[idx]}.py', 'w', encoding='utf8') as py_file:
        py_file.write(f'{file_header[idx]}')