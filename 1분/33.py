# break

'''
- break
반복문 탈출
반복문 내에서 반복 수행 중인 동작을 즉시 멈추고 반복문을 탈출하는 역할
'''

drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    print(f'{x} 시청')