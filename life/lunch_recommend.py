# 점심 메뉴 랜덤으로 골라주는 프로그램

import random

def lunch_recommendation():

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

    print('''
    메뉴판
    ====================================
    ({kor}){0:<10}{1:^5}{2:>10}{won}
    ({kor}){3:<10}{4:^5}{5:>10}{won}
    ({jpn}){6:<10}{7:^5}{8:>10}{won}
    ({jpn}){9:<10}{10:^5}{11:>10}{won}
    ({chi}){12:<10}{13:^5}{14:>10}{won}
    ({ita}){15:<10}{16:^5}{17:>10}{won}
    ====================================
    '''.format(menus[0], "'깔끔해요'", price[0],
                menus[1],"'매워요ㅜ'", price[1],
                menus[2], "'국물이 짱'", price[2],
                menus[3], "'원조의 맛'", price[3],
                menus[4], "'정통요리'", price[4],
                menus[5], "'존맛탱!'", price[5],
                kor="한식",
                jpn="일식",
                chi="중식",
                ita="양식",
                won="원"))

    choice = random.randrange(0, len(menus))

    print('''
    오늘의 메뉴 선택 : {}
    메뉴의 가격 : {}
    '''.format(menus[choice], price[choice]))
