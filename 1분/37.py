# 함수

'''
- 함수
어떤 동작을 수행하는 코드들의 묶음
여러 곳에서 사용되는 코드는 하나의 함수로 묶으면 굉장히 편리함

def 함수명():
    수행할 문장

함수를 정의만 했을 떄는 아무 동작을 하지 않음
함수 내의 문장을 실행시키기 위해 호출이라는 것이 필요함
'''

# 함수 정의
def show_price():
    print('커트 가격은 10000 원입니다')

# 함수 적용 및 호출
customer1 = '나장발'
print(f'{customer1} 고객님')
show_price()

customer2 = '나수염'
print(f'{customer2} 고객님')
show_price()