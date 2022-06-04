# 파일 만들기

file_path = './기본편/11-모듈과패키지/'
file_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
file_header = ['# 모듈', '# 패키지', '# __all__', '# 모듈 직접 실행', '# 패키지, 모듈 위치', '# pip install', '# 내장함수', '# 외장함수', '# 퀴즈']

for idx in range(len(file_list)):
    with open(f'{file_path}11-{file_list[idx]}.py', 'w', encoding='utf8') as py_file:
        py_file.write(f'{file_header[idx]}')