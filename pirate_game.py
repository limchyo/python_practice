import random

pirate_values = ['01', '02', '03', '04', '05',
                '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15',
                '16', '17', '18']


penalty_num1 = random.randint(1, 18)
penalty_num2 = penalty_num1
while penalty_num2 == penalty_num1:
    penalty_num2 = random.randint(1, 18)

# print(penalty_num1, penalty_num2)

kill_num = 0
while penalty_num1 != kill_num and penalty_num2 != kill_num:

    print('''
    해적통 게임 프로그램입니다!

               ---------
              |+++++++++|
              ____________
              |  O   @  |
              |    o    |
               ---===---
                 |   |
          ---------------------
          | {} | {} | {} | {} |
        --------------------------
        | {} | {} | {} | {} | {} |
        --------------------------
        | {} | {} | {} | {} | {} |
        --------------------------
          | {} | {} | {} | {} |
          ---------------------
    '''.format(pirate_values[0], pirate_values[1], pirate_values[2], pirate_values[3],
            pirate_values[4], pirate_values[5], pirate_values[6], pirate_values[7],
            pirate_values[8], pirate_values[9], pirate_values[10], pirate_values[11],
            pirate_values[12], pirate_values[13], pirate_values[14], pirate_values[15],
            pirate_values[16], pirate_values[17]))


    kill_num = int(input("칼 꽂을 번호를 입력하세요 : "))

    pirate_values[kill_num - 1] = "//"


print('''
            ---------
           |+++++++++|
           ___________
           |  O   @  |
           |    o    |
            ---===---
              |   |
              ~ /
              / ~ /
               /
              /   ~/
                / ~
             ~~  ~
퐁~~~~ 당신이 걸렸습니다!
''')
