# 문자열 처리

'''
문자열 처리

- 길이
len()

- 여러 줄 문자
변수 = """ 값 1
값 2
값 3 """
'''

snack = '꿀꽈배기'
two = '2개'

juseyo = snack + two # 꿀꽈배기2개
juseyo += '주세요' # 꿀꽈배기2개주세요

print(len(juseyo)) # 9

snack_info = """꿀꽈배기는
너무
맛있어요 """

print(snack_info) # 여러 줄 문자열 출력