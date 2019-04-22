# 비만도 계산기

print("비만도계산기 프로그램입니다")

gender = input("성별이 어떻게 되십니까?\n1. 남자\n2. 여자\n")
# gender = input('''
# 성별이 어떻게 되십니까?
# 1. 남자
# 2. 여자
# ''')
height = int(input("신장을 입력해주세요 : "))
weight = int(input("체중을 입력해주세요 : "))
age = input("나이를 입력해주세요 : ")

# gender = int(gender)
# height = int(height)
# weight = int(weight)
# age = int(age)

BMI = weight / (height * height/10000)

if BMI >= 35:
    result = "비만입니다. 꼭 살을 빼세요!"
elif BMI < 35 and BMI >= 30:
    result = "중등도 비만입니다. 다이어트가 필요해요!"
elif BMI < 30 and BMI >= 25:
    result = "경도 비만입니다. 식사량을 조금 줄여봐요!"
elif BMI < 24.9 and BMI >= 23:
    result = "과체중입니다. 체중 관리가 필요해요!"
elif BMI < 22.9 and BMI >= 18.5:
    result = "정상입니다. 유지에 노력해주세요!"
else:
    result = "저체중입니다. 체중을 늘릴 수 있도록 운동해요!"

# round(변수, 소수점자릿수) 메서드는 지정한 값만큼 반올림하여 자릿수 제한

print('''
당신의 BMI 수치는 {}입니다.

{}
'''.format(round(BMI, 2), result))
