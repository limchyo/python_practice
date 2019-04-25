import random

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

print('''
랜덤 로또 발생기 입니다.
당첨 번호 : {}, {}, {}, {}, {}, {}
2등 보너스 볼 : {}
'''.format(values[0], values[1],
            values[2], values[3],
            values[4], values[5],
            values[6]))
