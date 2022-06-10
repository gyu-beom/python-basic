# 기본값

'''
- 기본값
전달값에 기본으로 사용되는 값

def 함수명(전달값=기본값):
    수행할 문장
'''

# True : 단골 손님, False : 일반 손님
def get_price(is_vip=False):
    if is_vip == True:
        return 10000 # 단골 손님
    else:
        return 15000 # 일반 손님

price1 = get_price(True) # 단골 손님
price2 = get_price() # 일반 손님
price3 = get_price() # 일반 손님
price4 = get_price() # 일반 손님