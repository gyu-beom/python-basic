# 모듈

'''
- 모듈
코드들이 작성되어 있는 하나의 파이썬 파일 (변수, 함수, 클래스 등)

- 모듈 사용법
1. import 모듈
2. from 모듈 import 변수, 함수, 클래스

- import 방법
모듈 전체를 가지고 와서 모듈에 포함된 모든 기능을 다 사용하겠다는 의미

- from import 방법
모듈 중에서 필요한 것들만 사용하겠다는 의미
'''

# import 방식
# import goodjob
# goodjob.say()

# from import 방식
# from goodjob import say
# say()

import random
my_list = ['가위', '바위', '보']
print(random.choice(my_list))