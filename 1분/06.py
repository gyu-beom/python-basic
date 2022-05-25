# 형 변환

'''
형 변환

정수로 : int()
실수로 : float()
문자로 : str()
'''

print(int('2')) # int 2
print(float('1.5')) # float 1.5
print(str(2)) # str 2

# 실수에서 정수로 형 변환 주의사항
# - 실수 문자는 float로 먼저 형 변환하고
# - float 형 변환된 값을 int로 형 변환한다.
# - int로 형 변환 시, 소수점 이하는 버림.
print(int(float('2.5'))) # int 2