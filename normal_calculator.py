'''
일반계산기 프로그램 만들기

print("일반계산기 프로그램입니다!")
value1 = int(input("계산할 첫번째 값을 입력해주세요 : "))
value2 = int(input("계산할 두번째 값을 입력해주세요 : "))


print('''
# 두 개의 값 : {0} 와 {1}
#
# 더하기 값 (a + b) : {2}
# 빼기 값 (a - b) : {3}
# 곱하기 값 (a * b) : {4}
# 정수 나누기 값 (a // b) : {5}
# 실수 나누기 값 (a / b) : {6}
# 나머지 값 (a % b) : {7}
'''.format(value1, value2,
            value1 + value2,
            value1 - value2,
            value1 * value2,
            value1 // value2,
            value1 / value2,
            value1 % value2))
'''

print("일반계산기 프로그램입니다!")
value1 = int(input("계산할 첫번째 값을 입력해주세요 : "))
value2 = int(input("계산할 두번째 값을 입력해주세요 : "))
calculator_way = int(input('''
원하는 연산을 선택하세요.
1. 더하기
2. 빼기
3. 곱하기
4. 정수나누기
5. 실수나누기
6. 나머지 구하기
'''))

if calculator_way == 1:
    way = "더하기 값 (a + b)"
    result = value1 + value2
elif calculator_way == 2:
    way = "빼기 값 (a - b)"
    result = value1 - value2
elif calculator_way == 3:
    way = "곱하기 값 (a * b)"
    result = value1 * value2
elif calculator_way == 4:
    way = "정수 나누기 값 (a // b)"
    result = value1 // value2
elif calculator_way == 5:
    way = "실수 나누기 값 (a / b)"
    result = value1 / value2
elif calculator_way == 6:
    way = "나머지 구하기 (a % b)"
    result = value1 % value2
else:
    print("잘못 입력하셨습니다. 다시 실행해주세요.")

print('''
두 개의 값 : {} 와 {}
{} : {}
'''.format(value1, value2, way, result))
