# 퀴즈 3

'''
사이트 별로 비밀번호를 만들어주는 프로그램 작성

규칙 1 : http:// 부분은 제외
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외
규칙 3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!' 로 구성
'''

url = 'http://naver.com' # nav51!
# url = 'http://daum.net' # dau40!
# url = 'http://google.com' # goo61!
# url = 'http://youtube.com' # you71!

'''
< 내 풀이 >
rule1 = url.replace('http://','')
rule2 = rule1[:rule1.index('.')]
rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count('e')) + '!'

print(rule3)
'''

# < 나도코딩 풀이 >
my_str = url.replace('http://', '')
my_str = my_str[:my_str.index('.')]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print(F'{url}의 비밀번호는 {password} 입니다.')