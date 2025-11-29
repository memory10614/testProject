# score = int(input("점수를 입력하세요."))
#
# if score > 100 or score < 0:
#     print("정상적인 점수 범위가 아닙니다.")
# elif score >= 80:
#     print("합격입니다.")
# elif score >= 60:
#     print("재시험 응시가 필요합니다.")
# else:
#     print("불합격입니다.")
#
#     #while True:
#     #user_input = input("값을 입력하세요.")
#     #if user_input.lower() == "z":
#     #break
#
# input_number = int(input("숫자를 입력하세요."))
# index =2
#
# while index < input_number:
#     print(index)
#     index = index + 2
#
# print("피보나치 수열")
#     list = [1, 1]
#     last_item = list[len(list) - 1]
#
#     while last_item <= input_number:
#         print(last_item)
#         list.append(last_item + list[len(list) - 2])
#         last_item = list[len(list) - 1]
#
# print("피보나치 수열")
#         list = [1, 1]
#
#         while list[-1] < input_number:
#             print(list[-1])
#             list.append(list[-1] + list[-2])
# print("피보나치 수열")
#
#         a = 1
#         b = 1
#         c = 1
#
#         while c <= input_number:
#             print(c)
#             c = a + b
#             a = b
#             b = c
#
# def pirnt_usingif():
#     if score = int(input("점수를 입력하세요."))

# 답안의 key 기준으로 반복하는 방법
for key in correct_answer.keys():
    score = get_score(student[key], correct_answer[key])
    print(key, ": ",score)

# student key 기준으로 반복하는 방법
# for key in student.keys():
#     if key == 'name' or key == 'number':
#         continue
#     score = get_score(student[key], correct_answer[key])
#     print(key, ": ",score)