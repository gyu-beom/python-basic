# 패키지, 모듈 위치

'''
- 패키지, 모듈 위치
inspect : 모듈에 대한 경로 확인 모듈
getfile() : 파일 경로값 확인
'''

# import inspect
# import random

# print(inspect.getfile(random)) # /usr/lib/python3.x/random.py

# import inspect
# from travel import *

# print(inspect.getfile(thailand)) # $HOME/기본편/11-모듈과패키지/travel/thailand.py

'''
- 지금부터 하는 실습
현재 travel의 경로를 /usr/lib/python3.x 로 옮겨서 출력해보기

1. travel 디렉터리 복사하여 /usr/lib/python3.x 에 붙여넣기
2. travel 이름 travel_tmp 변경
3. inspect.getfile() 활용해서 travel 경로 출력
4. 원복
'''

# 1. 현재 travel 디렉터리 /usr/lib/python3.x 에 붙여넣기
# sudo cp -r travel/ /usr/lib/python3.x
# sudo ls -al /usr/lib/python3.x/travel

# 2. travel 이름 travel_tmp 변경
# mv travel travel_tmp

# 3. inspect.getfile() 활용해서 travel 경로 출력
# import inspect
# from travel import *

# print(inspect.getfile(thailand)) # /usr/lib/python3.x/travel/thailand.py

# 4. 원복
# sudo rm -rf /usr/lib/python3.x/travel
# mv travel_tmp travel
import inspect
from travel import *

print(inspect.getfile(thailand)) # $HOME/기본편/11-모듈과패키지/travel/thailand.py