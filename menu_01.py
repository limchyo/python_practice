메뉴판 만들기

1. 따옴표 사용하여 줄바꿈 자유롭게 하기
2. "format" 메소드 활용하기 (정렬, 빈칸 차지, 2개 이상 값 넣기 등)

print('''
메뉴판
=========================
{0:<10}{1:>10}{won}
{2:<10}{3:>10}{won}
{4:<10}{5:>10}{won}
=========================
'''.format("갈비탕", 10000,
            "떡볶이", 7000,
            "오뎅", 5000,
            won="원"))
