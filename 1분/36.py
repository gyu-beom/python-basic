# 리스트 컴프리핸션

'''
- 리스트 컴프리핸션
리스트 내에서 어떤 조건에 해당하는 데이터만 뽑아내거나 값을 바꿔서 새로운 리스트를 만들 때 사용

새로운_리스트 = [변수 활용 for 변수 in 반복대상 if 조건]
'''
# 리콜 대상 제품 조회
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [] # 리콜 대상 제품 리스트
for p in products:
    if p.startswith('SIRO'):
        recall.append(p)
print(recall)

# 리콜 대상 제품 조회 (리스트 컴프리핸션)
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [p for p in products if p.startswith('SIRO')]
print(recall)

# 리스트 컴프리핸션 예제
my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]
print(new_list)
# (1) my_list 에서
# (2) 3보다 큰 값들만
# (3) 그대로 사용해서
# (4) 새로운 리스트로 만들어 줘

# 리스트 컴프리핸션의 다양한 예제 1
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
# 모든 모델명 뒤에 SE (Special Edition) 을 붙여줘
prod_se = [p + 'SE' for p in products]
print(prod_se)

# 리스트 컴프리핸션의 다양한 예제 2
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
# 모든 모델명을 소문자로 바꿔줘
prod_lower = [p.lower() for p in products]
print(prod_lower)


# 리스트 컴프리핸션의 다양한 예제 3
# < 내 풀이 >
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
# 22년 제품만 뽑는데 뒤에 (최신형) 이라는 글자를 붙여줘
prod_new = [p + '(최신형)' for p in products if p[-2:] == '22']
print(prod_new)

# 리스트 컴프리핸션의 다양한 예제 3
# < 내 풀이 >
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
# 22년 제품만 뽑는데 뒤에 (최신형) 이라는 글자를 붙여줘
prod_new = [p + '(최신형)' for p in products if '2022' in p]
print(prod_new)

# 리스트 컴프리핸션의 다양한 예제 3
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
# 22년 제품만 뽑는데 뒤에 (최신형) 이라는 글자를 붙여줘
prod_new = [p + '(최신형)' for p in products if p.endswith('2022')]
print(prod_new)