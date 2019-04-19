# 일반계산기 프로그램 만들기

print("일반계산기 프로그램입니다!")
value1 = int(input("계산할 첫번째 값을 입력해주세요 : "))
value2 = int(input("계산할 두번째 값을 입력해주세요 : "))


print('''
두 개의 값 : {0} 와 {1}

더하기 값 (a + b) : {2}
빼기 값 (a - b) : {3}
곱하기 값 (a * b) : {4}
정수 나누기 값 (a // b) : {5}
실수 나누기 값 (a / b) : {6}
나머지 값 (a % b) : {7}
'''.format(value1, value2,
            value1 + value2,
            value1 - value2,
            value1 * value2,
            value1 // value2,
            value1 / value2,
            value1 % value2))
