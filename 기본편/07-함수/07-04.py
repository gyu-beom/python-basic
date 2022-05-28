# 키워드 인자

'''
- 키워드 인자
어떤 함수에 전달값들이 많고 기본값들이 잘 정의되어 있을때, 대부분 기본값을 쓰고 필요한 부분만 꼭 찍어서 값을 전달
순서에 구애받지 않음
'''

def profile(name, age, main_lang):
  print(name, age, main_lang)

profile(name='유재석', main_lang='파이썬', age=20)
profile(main_lang='자바', age=25, name='김태호')