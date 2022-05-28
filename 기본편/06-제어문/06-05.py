# 한 줄 for

'''
- 한 줄 for
[변수로 어떤 동작 for 변수 in 반복대상]
'''

student = [1, 2, 3, 4, 5]
print(student)

# 한 줄 for : 각 항목에 100 더하기
student = [i + 100 for i in student]
print(student)

students = ['Iron man', 'Thor', 'I am groot']
print(students)

# 한 줄 for : 각 항목의 길이 정보 반환
students = [len(i) for i in students]
print(students)

students = ['Iron man', 'Thor', 'I am groot']
print(students)

# 한 줄 for : 각 항목 대문자 변환
students = [i.upper() for i in students]
print(students)