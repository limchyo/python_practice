# 비만도 계산기

print("비만도계산기 프로그램입니다")

gender = input("성별이 어떻게 되십니까?\n1. 남자\n2. 여자\n")
# gender = input('''
# 성별이 어떻게 되십니까?
# 1. 남자
# 2. 여자
# ''')
height = input("신장을 입력해주세요 : ")
weight = input("체중을 입력해주세요 : ")
age = input("나이를 입력해주세요 : ")

# gender = int(gender)
height = int(height)
weight = int(weight)
# age = int(age)

BMI = weight / (height * height/10000)

# round(변수, 소수점자릿수) 메서드는 지정한 값만큼 반올림하여 자릿수 제한

print("당신의 BMI 수치는 {}입니다".format(round(BMI, 2)))
