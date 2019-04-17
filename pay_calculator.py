# 급여계산기

# 현재 최저시급 8,350원

pay = 8350
time_of_day = 8
day_of_month = 20

# 월급
profit = pay * time_of_day * day_of_month

print("급여계산기 프로그램입니다!")
print("예상 월급은 : {}원입니다".format(profit))
print("PC방 (1200원 기준) : {}시간".format(profit // 1200))
print("점심 (7000원 기준) : {}끼".format(profit // 7000))
print("영화 (10000원 기준) : {}편".format(profit // 10000))
print("노래방 (20000원 기준) : {}시간".format(profit // 20000))
