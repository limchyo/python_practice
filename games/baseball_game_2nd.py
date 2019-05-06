import random

def baseball():
    print("야구 게임입니다.")

    computer = list()

    while len(computer) != 4:
        num = random.randint(0, 9)
        if num not in computer:
            computer.append(num)

    # print(computer)

    count = 0
    strike = 0
    while strike != 4:
        player = input("답을 맞추어 보세요 : ")

        count += 1
        strike = 0
        ball = 0

        for index, value in enumerate(player):
            # print("index : {}, value : {}".format(index, value))
            if int(value) == computer[index]:
                strike += 1
            elif int(value) in computer:
                ball += 1

        if strike == 0 and ball == 0:
            print("Out!!")
        else:
            print("{} 스트라이크 {} 볼입니다.".format(strike, ball))

    print("{}번 만에 정답을 맞추셨습니다".format(count))
