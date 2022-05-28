# 튜플

'''
- 튜플
변수 = (값1, 값2, ...)

리스트의 '읽기 전용 버전'
데이터 변경이나 추가, 삭제 등 불가
대신 리스트보다 속도 빠름
'''

menu = ('돈가스', '치즈가스')
print(menu[0])
print(menu[1])

name = '김종국'
age = 20
hobby = '코딩'
print(name, age, hobby)

(name, age, hobby) = ('김종국', 20, '코딩')
print(name, age, hobby)