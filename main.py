from calculators import (
    grade_calculator_with_repeat,
    normal_calculator_repeat,
    obesity_calculator,
    pay_calculator_input
)
from games import (
    baseball_game_2nd, 
    baskin_robbins_game,
    crocodile_game,
    rsp_game_repeat
)


if __name__ == "__main__":

    while True:


        choice = int(input('''
실행하고자 하는 번호를 입력해주세요.
0. 종료
1. 학점 계산기
2. 일반 계산기
3. 비만도 계산기
4. 급여 계산기
5. 야구 게임
6. 배스킨라빈스 게임
7. 악어 게임
8. 가위바위보 게임

선택 : '''))

        if choice == 1:
            grade_calculator_with_repeat.calculate_grade()
        elif choice == 2:
            normal_calculator_repeat.calculate_two_numbers()
        elif choice == 3:
            obesity_calculator.calculate_obesity()
        elif choice == 4:
            pay_calculator_input.calculate_pay()
        elif choice == 5:
            baseball_game_2nd.baseball()
        elif choice == 6:
            baskin_robbins_game.baskin_robbins()
        elif choice == 7:
            crocodile_game.crocodile()
        elif choice == 8:
            rsp_game_repeat.r_s_p()
        elif choice == 0:
            print("프로그램을 종료합니다")
            break
