# pip install

'''
- pip install
https://pypi.org

sudo pip install beautifulsoup4

- pip 명령
install : 패키지 설치 : pip install [패키지]
install --upgrade : 패키지 업그레이드 : pip install --upgrade [패키지]
uninstall : 패키지 삭제 : pip uninstall [패키지]
list : 설치 패키지 목록 : pip list
show : 패키지 상세 정보 : pip show [패키지]
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Some<b>bad<i>HTML', features='html.parser')
print(soup.prettify())