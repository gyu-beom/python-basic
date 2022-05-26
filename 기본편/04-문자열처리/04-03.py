# 문자열처리함수

'''
- 문자열처리함수

소문자로 변환 : lower()
대문자로 변환 : upper()
대문자인지 확인 : isupper()
소문자인지 확인 : islower()
길이 확인 : len()
문자열 바꾸기 : replace()
찾으려는 문자열의 인덱스 (없으면 에러) : index()
찾으려는 문자열의 인덱스 (없으면 -1) : find()
문자열이 나온 횟수 : count()
'''

python = 'Python is Amazing'

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

# 문자열처리함수 : index
index = python.index('n') # 처음으로 발견된 n 의 인덱스
print(index) # 5
index = python.index('n', index + 1) # 두번째로 발견된 n 의 인덱스
print(index) # 15

# 문자열처리함수 : find
find = python.find('n') # 처음으로 발견된 n 의 인덱스
print(find) # 5
find = python.find('n', find + 1) # 두번째로 발견된 n 의 인덱스
print(find) # 15

# 문자열처리함수 : count
print(python.count('n')) # 2