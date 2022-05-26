# 메소드 2

'''
- 메소드 = "기능"

- 문자열 메소드
사용 방법 : 문자열.메소드(...)

~로 시작하는지 : startswith()
~로 끝나는지 : endswith()
앞뒤 불필요한 부분 제거 (아무것도 넣지 않으면 문자열 앞 뒤 공백 제거) : strip()
단어 바꾸기 : replace()
단어 위치 찾기 (인덱스 값으로 반환) : find()
다른 문자들 사이 가운데 : center()

- Python 내장형 검색 후 문자열 메소드 공부
'''

s = '나도고등학교'

print(s.startswith('나도')) # True
print(s.endswith('초등학교')) # False

s = '...나도고등학교...'

print(s.strip('.')) # 나도고등학교

s = '나도고등학교'

print(s.replace('고등학교', '고교')) # 나도고교
print(s.find('학교')) # 4
print(s.center(10, '-')) # --나도고등학교-- : 총 10글자
