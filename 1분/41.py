# 키워드값

'''
- 키워드값
전달값의 대상을 정확하게 지정해주는 것을 의미
키워드값의 순서는 함수에 정의된 순서와 달라도 아무 상관이 없음
'''

def get_price(is_vip=False, is_birthday=False, is_membership=False, card=False, review=False, first_time=False):
    print(f'Vip 정보 : {is_vip}')
    print(f'Birthday 정보 : {is_birthday}')
    print(f'Membership 정보 : {is_membership}')
    print(f'Card 정보 : {card}')
    print(f'Review 정보 : {review}')
    print(f'First Time 정보 : {first_time}')

price = get_price(review=True, is_birthday=True)