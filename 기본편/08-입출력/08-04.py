# pickle

'''
- pickle
프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하거나 불러올 수 있게 해주는 모듈
pickle을 이용해서 저장되는 파일은 텍스트 (txt) 가 아닌 바이너리 (binary) 형태
때문에 파일 저장 혹은 파일 불러오기 등의 모드를 사용할 때는 뒤에 b를 붙임

dump(data, dest_file)
저장할 데이터 : data
데이터를 저장할 파일 : dest_file
'''

import pickle

# pickle 쓰기 dump(data, dest_file)
profile_file = open('./기본편/08-입출력/profile.pickle', 'wb') # 바이너리 (binary) 형태로 저장
profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
print(profile)

pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
profile_file.close()

# pickle 읽기 load(src_file)
profile_file = open('./기본편/08-입출력/profile.pickle', 'rb') # 읽을 때도 바이너리 (binary) 명시
profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장

print(profile)
profile_file.close()
