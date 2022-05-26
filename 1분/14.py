# 문자열 포맷

'''
- 문자열 포맷
1. {} + format
2. {N} + format (N : 0, 1, 2, ...)
3. f-string

'''

python = '파이썬'
java = '자바'

print(python + ' ' + java) # 파이썬 자바
print(python, java) # 파이썬 자바

# 다른 문장 속에 넣으려면?
print('개발 언어에는 ' + python + ', ' + java + ' 등이 있어요')
print('개발 언어에는',python,',',java,'등이 있어요')

# 1. {} + format
print('개발 언어에는 {}, {} 등이 있어요'.format(python, java))

# 2. {N} + format (N : 0, 1, 2, ...)
print('개발 언어에는 {0}, {1} 등이 있어요'.format(python, java))
print('개발 언어에는 {1}, {0} 등이 있어요'.format(python, java))

# 3. f-string
print(f'개발 언어에는 {python}, {java} 등이 있어요')