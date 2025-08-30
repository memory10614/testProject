while True:
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "z":
        break

        print_times_table(int(user_input))