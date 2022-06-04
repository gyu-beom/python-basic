# __all__

'''
- __all__
패키지를 만든 사람이 공개 범위를 설정해줄 수 있음
즉, 패키지에 포함된 모듈 중에서 import 되기를 원하는 것만 공개를 하고 나머지는 비공개로 둘 수 있음

ex)
travel 패키지를 만들 때 함께 생성했던 __init__.py 파일에 __all__ 변수에 리스트 형태로 공개하려는 모듈 이름 추가
'''

from travel import *

# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()