def calculate_grade():
    print("학점계산기 프로그램입니다!")
    subject_count = int(input("신청한 과목 수를 입력해주세요: "))

    subjects = list()
    subject_scores = list()
    subject_grades = list()

    while len(subjects) != subject_count:
        subjects.append(input("과목명을 입력해주세요 : "))
        subject_scores.append(input("당신의 점수(A+ ~ F)를 입력해주세요 : "))
        subject_grades.append(input("취득한 학점을 입력해주세요 : "))

    calculating_way = int(input('''
    학점 계산 방식을 선택해주세요.
    1. 4.5 만점
    2. 4.3 만점
    '''))

    score = 0
    amount_of_grade = 0
    for index, subject_score in enumerate(subject_scores):
        # 취득한 학점 가져오기
        grade = int(subject_grades[index])
        # 총 취득한 학점
        amount_of_grade += grade

        if calculating_way == 1:
            if subject_score == "A+":
                score += 4.5 * grade
            elif subject_score == "A":
                score += 4.0 * grade
            elif subject_score == "B+":
                score += 3.5 * grade
            elif subject_score == "B":
                score += 3.0 * grade
            elif subject_score == "C+":
                score += 2.5 * grade
            elif subject_score == "C":
                score += 2.0 * grade
            elif subject_score == "F":
                score += 0
            else:
                score = "There is no value"

        elif calculating_way == 2:
            if subject_score == "A+":
                score += 4.3 * grade
            elif subject_score == "A":
                score += 4.0 * grade
            elif subject_score == "A-":
                score += 3.7 * grade
            elif subject_score == "B+":
                score += 3.3 * grade
            elif subject_score == "B":
                score += 3.0 * grade
            elif subject_score == "B-":
                score += 2.7 * grade
            elif subject_score == "C+":
                score += 2.3 * grade
            elif subject_score == "C":
                score += 2.0 * grade
            elif subject_score == "C-":
                score += 1.7 * grade
            elif subject_score == "F":
                score += 0
            else:
                score = "There is no value"

        else:
            print("잘못 입력하셨습니다. 프로그램이 종료됩니다.")
            break


    print('''
    취득한 총 학점 : {}
    당신의 GPA : {}
    '''.format(amount_of_grade, score/amount_of_grade))
