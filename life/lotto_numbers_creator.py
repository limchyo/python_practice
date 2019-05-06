import random

def lotto_creator():

    print("로또 번호 생성기 프로그램입니다!")

    values = list()

    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))
    # value.append(random.randrange(1, 46))

    while len(values) != 7:
        new_value = random.randrange(1, 46)
        if new_value not in values:
            values.append(new_value)

    # print('''
    # 랜덤 로또 발생기 입니다.
    # 당첨 번호 : {}, {}, {}, {}, {}, {}
    # 2등 보너스 볼 : {}
    # '''.format(values[0], values[1],
    #             values[2], values[3],
    #             values[4], values[5],
    #             values[6]))

    print("랜덤 로또 발생기 입니다.")
    # end=""는 개행(줄바꿈)을 막고, 이어서 문자를 지정할 수 있다
    print("당첨 번호 : ", end="")
    for index, value in enumerate(values):
        # 마지막 인덱스를 2등 보너스볼 숫자로 지정
        if index == len(values)-1:
            print("\n2등 보너스볼 : {0}".format(value))
        # 6개 숫자 연속적으로 출력
        else:
            print(value, end=' ')
