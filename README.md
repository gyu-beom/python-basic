# Python Basic

<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>

___

## ✋ Info
- [기본편](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/)
- [1분](/1%EB%B6%84/)
___

## 📌 Remember - 1분

### 1. 자료형 비교 [1분 파이썬 - 24.md](/1%EB%B6%84/24.md)

||리스트|튜플|세트|딕셔너리|
|:--|:--:|:--:|:--:|:--:|
|선언|lst = [ ]|t = ( )|s = { }|d = {key:val}|
|순서 보장|O|O|X|O (v3.7↑)|
|중복 허용|O|O|X|X (key)|
|인덱스 통한 접근|lst[idx]|t[idx]|X|d[key] <br> d.get(key)|
|수정|O|X|X|O (value)|
|추가|append() <br> insert() <br> extend()|X|add() <br> update()|d[key] = val <br> update()|
|삭제|remove() <br> pop() <br> clear()|X|remove() <br> discard() <br> pop() <br> clear()|pop() <br> popitem() <br> clear()|

- 리스트 : 여러 값들을 순서대로 관리할 때
- 튜플 : 값이 바뀔 일이 없거나, 바뀌면 안될 때
- 세트 : 값의 존재 여부가 중요, 중복은 안될 때
- 딕셔너리 : 키를 통해 효율적으로 관리하고 싶을 때

### 2. if 조건문 2 [1분 파이썬 - 27.py](/1%EB%B6%84/27.py)

- if 조건이 참이면 elif, else 조건은 실행하지 않음
```python
temp = 40
if temp >= 39:
    print('고열입니다')
elif temp >= 38:
    print('미열입니다')
else:
    print('정상입니다')
# 결과 : 고열입니다
```

___

## 📌 Remeber - 기본편

### 1. 다양한 출력포맷 순서 [기본편 파이썬 - 08-02.py](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/08-%EC%9E%85%EC%B6%9C%EB%A0%A5/08-02.py)

- [[빈자리채우기]정렬][기호][확보공간][콤마][.자리수][타입]
```python
# f-string 자리
print(f'{500}')
print(f'{500: >10}')
print(f'{500: >+10}')
print(f'{-500: >+10}')
print(f'{500:_<10}')

# f-string 콤마
print(f'{100000000000:,}')
print(f'{100000000000:+,}')
print(f'{-100000000000:+,}')

# f-string 복잡한 예제
print(f'{100000000000:^<+30,}')

# f-string 실수 (반올림 기본)
print(f'{5/3:f}')
print(f'{5/3:.2f}')
```

### 2. 비슷한 형태의 파일 만들기 [기본편 파이썬 - 10-00.py](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/10-%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC/10-00.py)

```python
file_path = './기본편/10-예외처리/' # 상대경로
file_list = ['01', '02', '03', '04', '05'] # 파일의 수 만큼 양식 지정
file_header = ['# 예외처리', '# 에러 발생시키기', '# 사용자 정의 예외처리', '# finally', '# 퀴즈'] # 파일의 상단 문구 지정

for idx in range(len(file_list)):
    with open(f'{file_path}10-{file_list[idx]}.py', 'w', encoding='utf8') as py_file:
        py_file.write(f'{file_header[idx]}')
```

### 3. 에러 발생시키기 [기본편 파이썬 - 10-03.py](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/10-%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC/10-03.py)

- 사용자 정의 에러를 만들기 위해서는 Exception 을 상속받는 클래스를 만들어야 함
- __init__() 을 통해 상세한 에러 메세지인 msg 멤버변수 정의
- __str__() 을 통해 msg 멤버변수 출력

```python
class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "[에러코드 001]" + self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기입니다')
    num1 = int(input('첫 번째 숫자를 입력하세요 : '))
    num2 = int(input('두 번째 숫자를 입력하세요 : '))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError(f'입력값 : {num1}, {num2}') # 자세한 에러 메시지
    print(f'{num1} / {num2} = {int(num1 / num2)}')
except ValueError:
    print('잘못된 값을 입력하였습니다 | 한 자리 숫자만 입력하세요')
except BigNumberError as err: # 사용자 정의 에러
    print('에러가 발생하였습니다 | 한 자리 숫자만 입력하세요')
    print(err)
```

### 4. 예외사항 퀴즈 [기본편 파이썬 - 10-05.py](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/10-%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC/10-05.py)

- 사용자 정의 에러 만들 때 반드시 __init__() 생성자 필요하지 않음

```python
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while(True):
    try:
        order = int(input('치킨 몇 마리 주문하시겠습니까? '))
        if order > chicken:
            print('재료가 부족합니다')
        # ValueError
        elif order <= 0:
            raise ValueError
        else:
            print(f'[대기번호 {waiting}] {order} 마리 주문이 완료되었습니다')
            waiting += 1
            chicken -= order
        # SoldOutError
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다')
    except SoldOutError:
        print('재고가 소진되어 더 이상 주문을 받지 않습니다')
        break
```

### 5. pip 명령어 [기본편 파이썬 - 11-06.py](/%EA%B8%B0%EB%B3%B8%ED%8E%B8/11-%EB%AA%A8%EB%93%88%EA%B3%BC%ED%8C%A8%ED%82%A4%EC%A7%80/11-06.py)

|옵션|설명|사용법|
|:--:|:--:|:--:|
|install|패키지 설치|pip install [패키지]|
|install --upgrade|패키지 업그레이드|pip install --upgrade [패키지]|
|uninstall|패키지 삭제|pip uninstall [패키지]|
|list|설치 패키지 목록|pip list|
|show|패키지 상세 정보|pip show [패키지]|
___

## 📜 Note
- [Python 내장형](https://docs.python.org/ko/3/library/stdtypes.html)
- [PEP8](https://peps.python.org/pep-0008/)
- [Python 외장함수](https://docs.python.org/3/py-modindex.html)
___