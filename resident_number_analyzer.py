'''
주민번호 분석기 만들기
1. 주민번호로 생년월일과 성별 분석하기
2. 주민번호로 출생지역 파악하기
'''

number = input("주민번호 분석기 프로그램입니다!\n주민번호를 입력해주세요 : ")

birth_year = number[0:2]
birth_month = number[2:4]
birth_day = number[4:6]
gender = number[6]
region = number[7:9]

region = int(region)

'''
충청남도 : 41 - 43, 45 - 47
세종특별자치시 :44, 96
전라북도 : 48 - 54
전라남도 : 55 - 66
광주광역시 : 55, 56
대구광역시 : 67 - 70
경상북도 : 71 - 81
경상남도 : 82 - 84, 86 - 90
울산광역시 : 85
제주특별자치도 : 91 - 95
'''

if region >= 0 and region <= 8:
    region = "서울특별시"
elif region >= 9 and region <= 12:
    region = "부산광역시"
elif region >= 13 and region <= 15:
    region = "인천광역시"
elif region >= 16 and region <= 25:
    region = "경기도"
elif region >= 26 and region <= 34:
    region = "강원도"
elif region >= 35 and region <= 39:
    region = "충청북도"
elif region == 40:
    region = "대전광역시"
elif region >= 41 and region <= 47:
    if region >= 41 and region <= 43:
        region = "충청남도"
    elif region >= 45 and region <= 47:
        region = "충청남도"
elif region == 44 or region == 96:
    region = "세종특별자치시"
elif region >= 48 and region <= 54:
    region = "전라북도"
elif region >= 55 and region <= 66:
    region = "전라남도"
elif region == 55 or region == 56:
    region = "광주광역시"
elif region >= 67 and region <= 70:
    region = "대구광역시"
elif region >= 71 and region <= 81:
    region = "경상북도"
elif region >= 82 and region <= 90:
    if region >= 82 and region <= 84:
        region = "경상남도"
    elif region >= 86 and region <= 90:
        region = "경상남도"
elif region == 85:
    region = "울산광역시"
elif region >= 91 and region <= 95:
    region = "제주특별자치도"

if gender == "1" or gender == "3":
    gender = "남자"

    print("생년월일 : {}년 {}월 {}일\n성별 : {}\n출생지역 : {}".format(birth_year, birth_month, birth_day, gender, region))

elif gender == "2" or gender == "4":
    gender = "여자"

    print("생년월일 : {}년 {}월 {}일\n성별 : {}\n출생지역 : {}".format(birth_year, birth_month, birth_day, gender, region))

else:
    print("잘못 입력하셨습니다. 다시 실행해주세요.")



'''
기타 정답
print("주민등록번호 분석기 프로그램입니다!")
​
resident_number = input("주민번호를 입력해주세요 : ")
​
# 생년 월일 탐색
birth_year = resident_number[0:2]
birth_month = resident_number[2:4]
birth_day = resident_number[4:6]
sex = resident_number[6]

# 성별 탐색
if sex == '1' or sex == '3':
    sex = '남자'
elif sex == '2' or sex == '4':
    sex = '여자'
else:
    sex = '중성'

# 지역 탐색
local_code = resident_number[7:9]
local_code = int(local_code)
​
if 0 <= local_code <= 8:
    local = '서울특별시'
elif 9 <= local_code <= 12:
    local = '부산광역시'
elif 13 <= local_code <= 15:
    local = '인천광역시'
elif 16 <= local_code <= 25:
    local = '경기도'
elif 26 <= local_code <= 34:
    local = '강원도'
elif 35 <= local_code <= 39:
    local = '충청북도'
elif local_code == 40:
    local = '대전광역시'
elif 41 <= local_code <= 43 or 45 <= local_code <= 47:
    local = '충청남도'
elif local_code == 44 or local_code == 96:
    local = '세종특별자치시'
elif 48 <= local_code <= 54:
    local = '전라북도'
elif 57 <= local_code <= 66:
    local = '전라남도'
elif 55 <= local_code <= 56:
    local = '광주광역시'
elif 67 <= local_code <= 70:
    local = '대구광역시'
elif 71 <= local_code <= 81:
    local = '경상북도'
elif 82 <= local_code <= 84 or 86 <= local_code <= 90:
    local = '경상남도'
elif local_code == 85:
    local = '울산광역시'
else:
    local = '제주특별자치도'
​
# 주민번호로부터 정보 출력
print("\n생년월일 : " + birth_year + "년 " + birth_month + "월 " + birth_day + "일")
print("성별 : " + sex)
print("출생지역 : " + local)
'''
