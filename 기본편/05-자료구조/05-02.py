# 사전

'''
- 사전
key와 value 쌍으로 구성
변수 = {키1:값1, 키2:값2, ...}

원하는 키의 값 출력 (에러 발생) : 사전[키]
원하는 키의 값 출력 (None 반환) : 사전.get(키)
원하는 값이 있는지 여부 확인 : 값 in 사전
원하는 키와 데이터 업데이트 또는 추가 : 사전[키] = 값
키, 데이터 삭제 : del 사전[키]
키만 출력 : 사전.keys()
값만 출력 : 사전.values()
키와 값 쌍으로 출력 : 사전.items()
전체 삭제 : 사전.clear()
'''

cabinet = {3: '유재석', 100: '조세호'}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 조세호
print(cabinet.get(3)) # 유재석

# 대괄호와 get() 차이점
# print(cabinet[5]) # 에러 발생
print(cabinet.get(5)) # None 반환

# get() 특징
print(cabinet.get(5, '사용 가능')) # 키 없을 때 기본값 출력

# in
print(3 in cabinet) # True
print(5 in cabinet) # False

# 키는 문자열도 가능
cabinet = {'A-3': '유재석', 'B-100': '김태호'}
print(cabinet['A-3']) # 유재석
print(cabinet['B-100']) # 김태호

# 업데이트 또는 추가
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 삭제
del cabinet['A-3'] # 키 'A-3' 및 데이터 삭제
print(cabinet)

# 키만 출력
print(cabinet.keys())

# 값만 출력
print(cabinet.values())

# 키, 값 쌍으로 출력
print(cabinet.items())

# 전체 삭제
cabinet.clear()
print(cabinet)