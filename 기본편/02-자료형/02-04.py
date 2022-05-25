# 변수

name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3 # age 값이 3 이상이면 True, 미만이면 False

print(f"우리집 {animal}의 이름은 {name}이에요.")
print(f"{name}는 {str(age)}살이며, {hobby}을 아주 좋아해요.") # 숫자 자료형은 문자열 자료형으로 형변환을 시키고 사용
print(f"{name}는 어른일까요? {str(is_adult)}")