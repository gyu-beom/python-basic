# 퀴즈

'''
표준 체중 구하는 프로그램
* 표준 체중 : 각 개인의 키에 적당한 체중

성별에 따른 공식
- 남자 : 키(m) * 키(m) * 22
- 여자 : 키(m) * 키(m) * 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
  - 함수명 : std_weight
  - 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

출력 예제
키 175cm 남자의 표준 체중은 67.35 입니다
'''

'''
< 내 풀이 >
def std_weight(height, gender):
  height = height / 100
  if gender == '남자':
    weight = round(height * height * 22, 2)
    return weight
  else:
    weight = round(height * height * 21, 2)
    return weight

height = 175
gender = '남자'

print(f'키 {height}cm {gender}의 표준 체중은 {std_weight(height, gender)}kg 입니다')
'''

def std_weight(height, gender):
  if gender == '남자':
    return height * height * 22
  else:
    return height * height * 21

height = 175
gender = '남자'
weight = round(std_weight(height / 100, gender), 2)
print(f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다')