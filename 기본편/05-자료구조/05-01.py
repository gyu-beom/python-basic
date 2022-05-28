# 리스트

'''
- 리스트
변수 = [값1, 값2, 값3, ...]

원하는 값의 인덱스 출력 : 리스트.index('값')
맨 뒤에 값 추가 : 리스트.append('값')
원하는 인덱스에 값 삽입 : 리스트.insert(인덱스, '값')
맨 뒤의 값 제거 : 리스트.pop()
원하는 값의 개수 : 리스트.count('값')
순서대로 정렬 : 리스트.sort()
역순으로 정렬 : 리스트.reverse()
리스트1에 리스트2 병합 : 리스트1.extend(리스트2)
'''

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '조세호', '박명수']
print(subway)
print(subway.index('조세호'))

subway.append('하하')
print(subway) # ['유재석', '조세호', '박명수', '하하']

subway.insert(1, '정형돈')
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append('유재석')
print(subway)
print(subway.count('유재석'))

num_list = [5, 4, 3, 2, 1]

num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

mix_list = ['조세호', 20, True]
print(mix_list)

num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)