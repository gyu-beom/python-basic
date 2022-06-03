# 전달값

'''
- 전달값
전달값 또는 파라미터
1. 여러 개 사용 가능 (콤마로 구분)
2. 함수 내에서만 사용

def 함수명(전달값):
    수행할 문장
'''

def show_price(customer):
    print(f'사랑하는 {customer} 고객님')
    print('감성 커트 가격은 15000 원입니다')

customer1 = '나장발'
show_price(customer1)

customer2 = '나수염'
show_price(customer2)