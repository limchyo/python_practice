# 메뉴판 만들기

# 따옴표 사용하여 줄바꿈 자유롭게 하기
# "format" 메소드 활용하기 (정렬, 빈칸 차지, 2개 이상 값 넣기 등)

# print('''
# 메뉴판
# =========================
# {0:<10}{1:>10}{won}
# {2:<10}{3:>10}{won}
# {4:<10}{5:>10}{won}
# =========================
# '''.format("갈비탕", 10000,
#             "떡볶이", 7000,
#             "오뎅", 5000,
#             won="원"))
#
#
# print('''
# 메뉴판
# ====================================
# ({kor}){0:<10}{1:^5}{2:>10}{won}
# ({kor}){3:<10}{4:^5}{5:>10}{won}
# ({kor}){6:<10}{7:^5}{8:>10}{won}
# ({jpn}){9:<10}{10:^5}{11:>10}{won}
# ({chi}){12:<10}{13:^5}{14:>10}{won}
# ({ita}){15:<10}{16:^5}{17:>10}{won}
# ====================================
# '''.format("갈비탕", "'깔끔해요'", 10000,
#             "떡볶이","'매워요ㅜ'", 7000,
#             "오뎅", "'국물이 짱'", 5000,
#             "초밥", "'원조의 맛'", 3000,
#             "짜장면", "'정통요리'",6000,
#             "스파게티", "'존맛탱!'", 8000,
#             kor="한식",
#             jpn="일식",
#             chi="중식",
#             ita="양식",
#             won="원"))

# menus = ["갈비탕", "떡볶이", "오뎅", "초밥", "짜장면", "스파게티"]
menus = list()
menus.append("갈비탕")
menus.append("떡볶이")
menus.append("오뎅")
menus.append("초밥")
menus.append("짜장면")
menus.append("스파게티")

# price = [10000, 7000, 5000, 3000, 6000, 8000]
price = list()
price.append(10000)
price.append(7000)
price.append(5000)
price.append(3000)
price.append(6000)
price.append(8000)

# print('''
# 메뉴판
# ====================================
# ({kor}){0:<10}{1:^5}{2:>10}{won}
# ({kor}){3:<10}{4:^5}{5:>10}{won}
# ({kor}){6:<10}{7:^5}{8:>10}{won}
# ({jpn}){9:<10}{10:^5}{11:>10}{won}
# ({chi}){12:<10}{13:^5}{14:>10}{won}
# ({ita}){15:<10}{16:^5}{17:>10}{won}
# ====================================
# '''.format(menus[0], "'깔끔해요'", price[0],
#             menus[1],"'매워요ㅜ'", price[1],
#             menus[2], "'국물이 짱'", price[2],
#             menus[3], "'원조의 맛'", price[3],
#             menus[4], "'정통요리'", price[4],
#             menus[5], "'존맛탱!'", price[5],
#             kor="한식",
#             jpn="일식",
#             chi="중식",
#             ita="양식",
#             won="원"))

print("메뉴판")
print("====================================")
for index, value in enumerate(menus):
    print("{0:<10}{1:>10}{won}".format(value, price[index], won="원"))
print("====================================")
