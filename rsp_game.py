# 가위 바위 보 게임

# print("가위 바위 보 게임입니다.")
# player1 = input('''
# 첫번째 플레이어 무엇을 낼 건가요?!
# 1. 가위
# 2. 바위
# 3. 보
# ''')
# player2 = input('''
# 두번째 플레이어 무엇을 낼 건가요?!
# 1. 가위
# 2. 바위
# 3. 보
# ''')

# print("첫번째 플레이어는 {}를 내셨습니다.".format(player1))
# print("두번째 플레이어는 {}를 내셨습니다.".format(player2))

print("가위 바위 보 게임입니다.")

player1 = int(input('''
첫번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
'''))

player2 = int(input('''
두번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
'''))

if player1 == 1:
    player1 = "가위"
elif player1 == 2:
    player1 = "바위"
elif player1 == 3:
    player1 = "보"
else:
    player1 = "*"

if player2 == 1:
    player2 = "가위"
elif player2 == 2:
    player2 = "바위"
elif player2 == 3:
    player2 = "보"
else:
    player2 = "&"

print('''
첫번째 플레이어는 {}를 내셨습니다.
두번째 플레이어는 {}를 내셨습니다.
'''.format(player1, player2))

if player1 == player2:
    print("비겼습니다")
elif player2 == "가위":
    if player1 == "바위":
        print("첫번째 플레이어가 바위로 승리하였습니다!")
    elif player1 == "보":
        print("두번째 플레이어가 가위로 승리하였습니다!")
elif player2 == "바위":
    if player1 == "보":
        print("첫번째 플레이어가 보로 승리하였습니다!")
    elif player1 == "가위":
        print("두번째 플레이어가 바위로 승리하였습니다!")
elif player2 == "보":
    if player1 == "가위":
        print("첫번째 플레이어가 가위로 승리하였습니다!")
    elif player1 == "바위":
        print("두번째 플레이어가 보로 승리하였습니다!")
else:
    print("잘못된 입력입니다. 다시 실행해주세요.")
