def calculate_two_numbers():
    print("일반계산기 프로그램입니다!")

    def add(num1, num2):
        result = num1 + num2
        return result

    def sub(num1, num2):
        result = num1 - num2
        return result

    def mul(num1, num2):
        result = num1 * num2
        return result

    def div_int(num1, num2):
        result = num1 // num2
        return result

    def div_float(num1, num2):
        result = num1 / num2
        return result

    def remainder(num1, num2):
        result = num1 % num2
        return result

    while True:
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
        7. 계산기 종료
        '''))


        if calculator_way == 1:
            way = "더하기 값 (a + b)"
            result = add(value1, value2)
            # result = value1 + value2
        elif calculator_way == 2:
            way = "빼기 값 (a - b)"
            result = sub(value1, value2)
            # result = value1 - value2
        elif calculator_way == 3:
            way = "곱하기 값 (a * b)"
            result = mul(value1, value2)
            # result = value1 * value2
        elif calculator_way == 4:
            way = "정수 나누기 값 (a // b)"
            result = div_int(value1, value2)
            # result = value1 // value2
        elif calculator_way == 5:
            way = "실수 나누기 값 (a / b)"
            result = div_float(value1, value2)
            # result = value1 / value2
        elif calculator_way == 6:
            way = "나머지 구하기 (a % b)"
            result = remainder(value1, value2)
            # result = value1 % value2
        elif calculator_way == 7:
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n잘못 입력하셨습니다. 다시 실행해주세요.")

        print('''
        두 개의 값 : {} 와 {}
        {} : {}
        '''.format(value1, value2, way, result))
