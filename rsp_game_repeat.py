import random

print("가위 바위 보 게임입니다.")

while True:

    player = int(input("\n무엇을 낼 건가요?!\n1. 가위\n2. 바위\n3. 보\n"))
    # computer = int(random.randrange(1, 4))
    computer = random.randint(1, 3)

    if player == 1:
        player = "가위"
    elif player == 2:
        player = "바위"
    elif player == 3:
        player = "보"
    else:
        print("\n잘못 입력하셨습니다.")
        continue

    if computer == 1:
        computer = "가위"
    elif computer == 2:
        computer = "바위"
    elif computer == 3:
        computer = "보"
    else:
        print("\n잘못 입력하셨습니다.")
        continue

    # print('''
    # 플레이어는 {}를 내셨습니다.
    # 컴퓨터는 {}를 냈습니다.
    # '''.format(player, computer))
    print("\n플레이어는 {}를 내셨습니다.\n컴퓨터는 {}를 냈습니다.\n"
    .format(player, computer))

    if player == computer:
        print("비겼습니다")
    elif computer == "가위":
        if player == "바위":
            print("플레이어가 바위로 승리하였습니다!")
            break
        elif player == "보":
            print("컴퓨터가 가위로 승리하였습니다!")
            # continue
    elif computer == "바위":
        if player == "보":
            print("플레이어가 보로 승리하였습니다!")
            break
        elif player == "가위":
            print("컴퓨터가 바위로 승리하였습니다!")
            # continue
    elif computer == "보":
        if player == "가위":
            print("플레이어가 가위로 승리하였습니다!")
            break
        elif player == "바위":
            print("컴퓨터가 보로 승리하였습니다!")
            # continue
    else:
        print("잘못된 입력입니다. 다시 실행해주세요.")
