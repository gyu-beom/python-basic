# 기본값

'''
- 기본값
굳이 무엇이다 라고 말하지 않아도 당연히 그것이겠거니 하는 내용
'''

def profile(name, age, main_lang):
  print(f'이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}')

profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 기본값
def profile(name, age=17, main_lang='파이썬'):
  print(f'이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}')

profile('유재석')
profile('김태호')