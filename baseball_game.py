import random

print("야구 게임 프로그램입니다!")

computer = list()

while len(computer) != 4:
    number1 = random.randrange(0, 10)
    if number1 not in computer:
        computer.append(number1)

# print(computer)
strike = 0
count = 0
while strike != 4:

    player = list()

    while len(player) != 4:
        number2 = int(input("답을 맞추어 보세요 : "))
        if number2 not in player:
            player.append(number2)
        else:
            print("중복입니다. 다시 입력해주세요.")

    strike = 0
    ball = 0

    for index, value in enumerate(player):
        # print(index, value)
        if value == computer[index]:
            strike += 1
        elif value in computer:
            ball += 1

    if strike == 0 and ball == 0:
        print("Out!\n")
    else:
        print("{} 스트라이크 {} 볼입니다\n".format(strike, ball))

    count += 1

print("{}번만에 정답을 맞추셨습니다!".format(count))
