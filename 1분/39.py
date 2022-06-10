# 반환값

'''
- 반환값
함수 내에서 어떤 동작이나 연산을 수행하고 나서 그 함수를 호출한 쪽으로 결과를 반환해줄 수 있음

def 함수명(전달값):
    수행할 문장
    return 반환값

1. 함수에서 반환값은 보통은 1개
2. 여러 개 반환 가능 (콤마로 구분, 튜플)
3. return 키워드를 통해 반환되는 즉시 함수 탈출
'''
# 함수 정의
def get_price():
    return 15000

# 함수 호출
price = get_price()
print(f'커트 가격은 {price} 원입니다')

# True : 단골 손님, False : 일반 손님
def get_price(is_vip):
    if is_vip == True:
        return 10000 # 단골 손님
    else:
        return 15000 # 일반 손님

price = get_price(True)
print(f'커트 가격은 {price} 원입니다')