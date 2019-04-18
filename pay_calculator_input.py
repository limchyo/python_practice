# 급여계산기 + 입력 받기

# 현재 최저시급 8,350원

# pay = 8350
# time_of_day = 8
# day_of_month = 20


print("급여계산기 프로그램입니다!")

pay = input("시급을 입력해주세요 : ")
time_of_day = input("일일근무시간 : ")
day_of_month = input("한달근무일수 : ")

pay = int(pay)
time_of_day = int(time_of_day)
day_of_month = int(day_of_month)

# 월급
profit = pay * time_of_day * day_of_month

print("예상 월급은 : {}원입니다\n\n".format(profit))
print("{}원으로 무엇을 할 수 있을까요?".format(profit))
print("PC방 (1200원 기준) : {}시간".format(profit // 1200))
print("점심 (7000원 기준) : {}끼".format(profit // 7000))
print("영화 (10000원 기준) : {}편".format(profit // 10000))
print("노래방 (20000원 기준) : {}시간".format(profit // 20000))
