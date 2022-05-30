# while

'''
- while
~ 하는 동안

- for vs while
for :  정해진 범위 또는 데이터를 순회하면서 반복
while : 조건이 참인 동안 계속해서 반복

while 조건:
    반복 수행 문장
'''

max = 25
weight = 0
item = 3

while weight + item <= max:
    weight += item
    print('짐을 추가합니다')
print(f'총 무게는 {weight} 입니다')