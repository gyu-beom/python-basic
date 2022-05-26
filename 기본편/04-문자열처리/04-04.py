# 문자열포맷

'''
- 1. %
print('문자열 %d 문자열' % 정수) # d : decimal
print('문자열 %c 문자열' % 문자) # c : character
print('문자열 %s 문자열' % 문자열) # s : string

- 2. .format()

- 3. f-string
'''

# 방법 1 : %
print('나는 %d살입니다.' % 20)
print('Apple은 %c로 시작해요.' % 'A')
print('나는 %s을 좋아합니다.' % '파이썬')
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

# 방법 2-1 : .format()
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))

# 방법 2-2 : .format()
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=20, color='빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color='빨간', age=20))

# 방법 3 : f-string
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')