# 딕셔너리 2

'''
- 딕셔너리
딕셔너리 = {key1:value1, key2:value2, ...}

원하는 키의 값에 접근 : 딕셔너리[키]
원하는 키의 값에 접근 (없는 key에 접근하면 None 출력) : 딕셔너리.get(키)
새로운 데이터 추가 또는 특정 키의 값 변경 : 딕셔너리[키] = 값
여러 키들의 값들을 변경 : 딕셔너리.update({키1:값1, 키2:값2, ...})
특정 키:값 삭제 : 딕셔너리.pop(키)
모든 데이터 삭제 : 딕셔너리.clear()
어떤 키들이 있는지 확인 : 딕셔너리.keys()
어떤 값들이 있는지 확인 : 딕셔너리.values()
어떤 키:값들이 있는지 확인 : 딕셔너리.items()
제공된 키들을 통해 새로운 딕셔너리 생성 및 반환 : fromkeys()
마지막으로 추가된 데이터 삭제 : popitem()
키에 해당되는 값 반환 (키가 없다면 새로 만들고 default value 설정 및 반환) : setdefault()
'''

person = {
    '이름': '나귀욤',
    '나이': 7,
    '키': 120,
    '몸무게': 23
}

print(person.get('별명')) # None

# 새로운 데이터 추가 또는 수정
person['최종학력'] = '유치원'
person['키'] = 130
print(person.get('최종학력'))
print(person.get('키'))

# 여러 key들의 value 변경
person.update({'키': 130, '몸무게': 26})
print(person.get('키'))
print(person.get('몸무게'))

# 특정 key:value 삭제
person.pop('몸무게')
print(person.get('몸무게'))

# 모든 데이터 삭제
person.clear()
print(person)

person = {
    '이름': '나귀욤',
    '나이': 7,
    '키': 120,
    '몸무게': 23
}
print(person)

# 어떤 key들이 있는지 확인
print(person.keys())

# 어떤 value들이 있는지 확인
print(person.values())

# 어떤 key:value들이 있는지 확인
print(person.items())