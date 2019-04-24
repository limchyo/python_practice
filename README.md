파이썬 숙달을 위한 연습 공간
============
1. 메뉴판 만들기
> `format` 메소드 활용 연습
```
메뉴판
=========================
갈비탕            10000원
떡볶이             7000원
오뎅              5000원
=========================
```
```
메뉴판
====================================
(한식)갈비탕       '깔끔해요'     10000원
(한식)떡볶이       '매워요ㅜ'      7000원
(한식)오뎅        '국물이 짱'      5000원
(일식)초밥        '원조의 맛'      3000원
(중식)짜장면       '정통요리'      6000원
(양식)스파게티      '존맛탱!'      8000원
====================================
```

1-1. 악어 그리기
> 숫자는 `foramt` 메소드를 사용하여 입력
```
        ------              -------
            0               0
  ------------------------------------
        0                       0
========================================
|01||02||03||04||05||06||07||08||09||10|
----------------------------------------

----------------------------------------
|11||12||13||14||15||16||17||18||19||20|
========================================
```

2. 급여계산기
> `변수` 활용 연습
```
급여계산기 프로그램입니다!
예상 월급은 : 1336000원입니다


1336000원으로 무엇을 할 수 있을까요?
PC방 (1200원 기준) : 1113시간점심 (7000원 기준) : 190끼
영화 (10000원 기준) : 133편
노래방 (20000원 기준) : 66시간
```

2.1 급여계산기 + 입력 받기
> `변수` 및 `input`, `int` 메서드를 활용 연습
```
급여계산기 프로그램입니다!
시급을 입력해주세요 : `8350` 
일일근무시간 : `8`
한달근무일수 : `20`
예상 월급은 : `1336000`원입니다


1336000원으로 무엇을 할 수 있을까요?
PC방 (1200원 기준) : 1113시간점심 (7000원 기준) : 190끼
영화 (10000원 기준) : 133편
노래방 (20000원 기준) : 66시간
```

> `if`문 활용 연습
```
급여계산기 프로그램입니다!
시급을 입력해주세요 : 8350
일일근무시간 : 8
한달근무일수 : 20

수습(90%)을 적용하나요?
1. 적용
2. 미적용
1

세금을 적용하나요?
1. 미적용
2. 4대 보혐료 공제(8.41%)
3. 소득세 공제(3.3%)
4. 모두 적용
4

총 세금 : 156445원을 제외한
예상 월급은 : 1045955원입니다


1045955원으로 무엇을 할 수 있을까요?
PC방 (1200원 기준) : 871시간
점심 (7000원 기준) : 149끼
영화 (10000원 기준) : 104편
노래방 (20000원 기준) : 52시간
```

3. 비만도 계산기(BMI 측정)
> `변수` 및 `input`, `int`, `round` 메서드를 활용 연습
```
비만도계산기 프로그램입니다
성별이 어떻게 되십니까?
1. 남자
2. 여자
`1`
신장을 입력해주세요 : `170`
체중을 입력해주세요 : `64`
나이를 입력해주세요 : `32`
당신의 BMI 수치는 22.15입니다
```
> `if`문 활용하여 비만 정도 확인하기
```
비만도계산기 프로그램입니다
성별이 어떻게 되십니까?
1. 남자
2. 여자
1
신장을 입력해주세요 : 170
체중을 입력해주세요 : 65
나이를 입력해주세요 : 32

당신의 BMI 수치는 22.49입니다.

정상입니다. 유지에 노력해주세요!
```

4. 가위 바위 보 게임
> `input`, `foramt` 메서드 연습
```
가위 바위 보 게임입니다.

첫번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
1

두번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
2

첫번째 플레이어는 1를 내셨습니다
두번째 플레이어는 2를 내셨습니다
```
> 가위바위로 및 승부 판별
> `다중조건문` 활용
```
가위 바위 보 게임입니다.

첫번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
2

두번째 플레이어 무엇을 낼 건가요?!
1. 가위
2. 바위
3. 보
3

첫번째 플레이어는 바위를 내셨습니다.
두번째 플레이어는 보를 내셨습니다.

두번째 플레이어가 보로 승리하였습니다!
```

5. 일반계산기 프로그램
> `input`, `int`, `foramt` 메서드 활용 연습
```
일반계산기 프로그램입니다!
계산할 첫번째 값을 입력해주세요 : 5
계산할 두번째 값을 입력해주세요 : 2

두 개의 값 : 5 와 2

더하기 값 (a + b) : 7
빼기 값 (a - b) : 3
곱하기 값 (a * b) : 10
정수 나누기 값 (a // b) : 2
실수 나누기 값 (a / b) : 2.5
나머지 값 (a % b) : 1
```
> `조건문` 활용하여 원하는 연산 방식을 선택하여 계산하도록 개선
```
일반계산기 프로그램입니다!
계산할 첫번째 값을 입력해주세요 : 45
계산할 두번째 값을 입력해주세요 : 10

원하는 연산을 선택하세요.
1. 더하기
2. 빼기
3. 곱하기
4. 정수나누기
5. 실수나누기
6. 나머지 구하기
6

두 개의 값 : 45 와 10
나머지 구하기 (a % b) : 5
```
6. 학점계산기 프로그램
> `다중조건문` 활용하기
```
과목명을 입력해주세요 : 대수학
당신의 점수(A+ ~ F)를 입력해주세요 : A+
취득한 학점을 입력해주세요 : 3

학점 계산 방식을 선택해주세요.
1. 4.5 만점
2. 4.3 만점
2

과목 이름 : 대수학
당신의 점수 : A+
변환한 점수 : 4.3
당신의 취득학점 : 3
```

7. 주민번호 분석기(생년월일, 성별, 지역 분석)
> 문자열 `indexing`, `slicing` 활용하기
```
주민번호 분석기 프로그램입니다!
주민번호를 입력해주세요 : 8808231**
생년월일 : 88년 08월 23일
성별 : 남자
출생지역 : 경상남도
```
