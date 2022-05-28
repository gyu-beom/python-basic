# 전달값과 반환값

'''
- 전달값과 반환값

def 함수이름 (전달값1, 전달값2, ...):
  실행 명령문1
  실행 명령문2
  ...
  return 반환값1, 반환값2, ...

전달값 : 매개변수 (parameter)
return : 탈출문자 (break와 비슷)
'''

def deposit(balance, money):
  print(f'임금이 완료되었습니다 잔액은 {balance + money} 원입니다')
  return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
  if balance >= money:
    print(f'출금이 완료되었습니다 잔액은 {balance - money} 원입니다')
    return balance - money
  else:
    print(f'출금이 완료되지 않았습니다 잔액은 {balance} 원입니다')
    return balance

balance = 0
balance = deposit(balance, 1000)

# 출금시도
balance = withdraw(balance, 2000) # 2000원 출금 시도 시 잔액 부족으로 실패
balance = withdraw(balance, 500) # 500원 출금 시도 시 성공
print(balance)

def withdraw_night(balance, money):
  commission = 100
  return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)

# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print(f'수수료 {commission} 원이며 잔액은 {balance} 원입니다')