# 패키지

'''
- 패키지
여러 모듈들을 모아 놓은 집합
패키지는 보통 하나의 폴더 안에 여러 모듈 파일들로 구성

- 사용한 패키지 디렉터리 : travel

import 구문을 사용할 때는 그 대상이 모듈이나 패키지어야 함, 클래스나 함수는 import 불가
'''

# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from ~ import
from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam

trip_to = vietnam.VietnamPackage()
trip_to.detail()