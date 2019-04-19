# 급여계산기 + 입력 받기

# 현재 최저시급 8,350원

# pay = 8350
# time_of_day = 8
# day_of_month = 20


print("급여계산기 프로그램입니다!")

# pay = input("시급을 입력해주세요 : ")
# time_of_day = input("일일근무시간 : ")
# day_of_month = input("한달근무일수 : ")

# pay = int(pay)
# time_of_day = int(time_of_day)
# day_of_month = int(day_of_month)

pay = int(input("시급을 입력해주세요 : "))
time_of_day = int(input("일일근무시간 : "))
day_of_month = int(input("한달근무일수 : "))

practice = int(input('''
수습(90%)을 적용하나요?
1. 적용
2. 미적용
'''))

tax = int(input('''
세금을 적용하나요?
1. 미적용
2. 4대 보혐료 공제(8.41%)
3. 소득세 공제(3.3%)
4. 모두 적용
'''))

# 월급
profit = pay * time_of_day * day_of_month

if practice == 1:
    practice_price = profit // 10
else:
    practice_price = 0

if tax == 2:
    tax_price = profit * 841 // 10000
elif tax == 3:
    tax_price = profit * 33 // 1000
elif tax == 4:
    tax_price = profit * 841 // 10000 + profit * 33 // 1000
else:
    tax_price = 0

profit = profit - practice_price - tax_price

print("\n총 세금 : {}원을 제외한".format(tax_price))
print("예상 월급은 : {}원입니다\n\n".format(profit))
print("{}원으로 무엇을 할 수 있을까요?".format(profit))
print("PC방 (1200원 기준) : {}시간".format(profit // 1200))
print("점심 (7000원 기준) : {}끼".format(profit // 7000))
print("영화 (10000원 기준) : {}편".format(profit // 10000))
print("노래방 (20000원 기준) : {}시간".format(profit // 20000))
