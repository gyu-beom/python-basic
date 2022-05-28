# 세트

'''
- 세트
변수 = {값1, 값2, ...}

중복 허용 X
순서 보장 X

교집합
  - 세트1.intersection(세트2)
  - 세트1 & 세트2
합집합
  - 세트1.union(세트2)
  - 세트1 | 세트2
차집합
  - 세트1.difference(세트2)
  - 세트1 - 세트2
추가 : 세트.add(값)
삭제 : 세트.remove(값)

세트는 순서를 보장하지 않기 때문에 매번 결과가 다름
'''

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

print(java)
print(python)

# 교집합 : intersection(), &
print(java & python)
print(java.intersection(python))

# 합집합 : union(), |
print(java | python)
print(java.union(python))

# 차집합 : difference(), -
print(java - python)
print(java.difference(python))

# 추가 : add()
python.add('김태호')
print(python)

# 제거 : remove()
java.remove('김태호')
print(java)