# 모듈

'''
- 모듈
부품만 교체하거나 추가할 수 있도록 만들면 유지보수도 쉽고 코드의 재사용도 수월해지는 장점
함수 정의나 클래스 등 서로 관련이 있거나 비슷한 기능을 하는 파이썬 문장들을 담고 있는 파일 : 모듈
필요한 것들끼리 부품처럼 잘 만드는 것 : 모듈화

- 사용한 모듈 : theater_module.py

import 모듈명 as 모듈의별명 : 모듈의 별명을 붙여 간편하게 호출
from 모듈명 import 모듈내사용할부분 : 모듈명. 필요없음, 콤마로 구분
from 모듈명 import 모듈내사용할부분 as 모듈내사용할부분의별칭
'''

# import theater_module

# theater_module.price(3)
# theater_module.price_moring(4)
# theater_module.price_solider(5)

# 모듈 별명
# import theater_module as mv

# mv.price(3)
# mv.price_moring(4)
# mv.price_solider(5)

# from ~ import
# from theater_module import *

# price(3)
# price_moring(4)
# price_solider(5)

# from ~ import ,
# from theater_module import price, price_moring

# price(3)
# price_moring(4)
# price_solider(5) # Error

# from ~ import as
from theater_module import price_solider as price
price(5) # price_solider() 호출