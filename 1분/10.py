# 인덱스와 슬라이싱

'''
- 파이썬 문자열, 리스트
몇 번째 = 리스트, 0번부터 시작

어디부터 : 어디 직전까지 = 슬라이싱
lang[start:end] # start 부터 end 직전까지
'''

lang = "PYTHON"
print(lang[0]) # P
print(lang[5]) # N
print(lang[-1]) # N

print(lang[1:6]) # YTHON
print(lang[1:]) # YTHON
print(lang[:4]) # PYTH
print(lang[:]) # PYTHON

fruit = 'apple'
print(fruit[:]) # apple
print(fruit[0:]) # apple
print(fruit[:5]) # apple
print(fruit[:-1]) # appl