import random

print("배스킨라빈스 31 게임 프로그램입니다!")

def validate_input(prompt, valid_list):
    while True:
        value = int(input(prompt))
        if value in valid_list:
            break
        else:
            print("잘못된 입력입니다. 재입력해주세요.")
    return value

def call_numbers(size, called):
    for _ in range(size):
        called += 1
        print("'{}'!!!".format(called))

        if called == 31:
            break

    return called

order = validate_input("순서를 입력하세요. (선공 1, 후공 0 입력) : ", [0, 1])

# while True:
#     order = int(input("순서를 입력하세요. (선공 1, 후공 0 입력) : "))
#     if order in [0, 1]:
#         break
#     else:
#         print("잘못된 입력입니다. 재입력해주세요.")


call = 0 # 호출수
count = 1 # 차례수
# 31번째가 되면 자동 종료
while call < 31:
    if count % 2 == order:
        print("사용자의 차례")

        size_of_call = validate_input("호출할 개수를 입력하세요 : ", [1, 2, 3])

        # while True:
        #     size_of_call = int(input("호출할 개수를 입력하세요 : "))
        #
        #     if size_of_call in [1, 2, 3]:
        #         break
        #     else:
        #         print("잘못된 입력입니다. 재입력해주세요.")

        call = call_numbers(size_of_call, call)

        # size_of_call의 수만큼 반복한다
        # for _ in range(size_of_call):
        #     call += 1
        #     print("사용자 : '{}'!!!".format(call))
        #
        #     if call == 31:
        #         break



    else:
        print("컴퓨터의 차례")
        size_of_call = random.randint(1, 3)

        # while True:
        #     if size_of_call in [1, 2, 3]:
        #         break
        #     else:
        #         print("잘못된 입력입니다. 재입력해주세요.")

        call = call_numbers(size_of_call, call)

        # for _ in range(size_of_call):
        #     call += 1
        #     print("컴퓨터 : '{}'!!!".format(call))
        #
        #     if call == 31:
        #         break


    count += 1


# print(count)
if count % 2 == order:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")
