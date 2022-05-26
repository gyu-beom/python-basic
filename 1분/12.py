# 메소드 1

'''
- 메소드
클래스 내에 정의된 어떤 동작, 기능을 하는 코드들의 묶음 => 기능

- 문자열 메소드
사용 방법 : 문자열.메소드(...)

소문자로 : lower()
대문자로 : upper()
첫 글자만 대문자로 : capitalize()
각 단어 첫 글자만 대문자로 : title()
대소문자 상호 변환 : swapcase()
문자열 분리 : split()
특정 단어의 수 : count()
'''

letter = 'how are YOU?'

print(letter.lower()) # how are you?
print(letter.upper()) # HOW ARE YOU?
print(letter.capitalize()) # How are you?
print(letter.title()) # How Are You?
print(letter.swapcase()) # HOW ARE you?
print(letter.split()) # ['how', 'are', 'YOU?']
print(letter.count('how')) # 1