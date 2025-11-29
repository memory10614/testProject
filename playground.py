import random

def UP_DOWN_게임():
    result = random.randint(1, 100)
    print("게임을 시작하지.")

    while True:
        user = int(input("1부터 100까지의 아무 숫자나 입력하시오."))
        if user < result:
            print("up")
        elif user > result:
            print("down")
        elif user == result:
            print("게임을 종료하지.")
            break