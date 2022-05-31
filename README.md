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


___

## 📜 Note
- [Python 내장형](https://docs.python.org/ko/3/library/stdtypes.html)
- [PEP8](https://peps.python.org/pep-0008/)
___