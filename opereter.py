#대입연산자
x = 10
y = 15



#조건연산자
z = x == y
print("x == y : ", z)
z = x != y
print("x != y : ", z)
z = x > y
print("x > y : ", z)
z = x >= y
print("x >= y : ", z)
z = x < y
print("x < y : ", z)
z = x <= y
print("x <= y : ", z)


#사칙연산
z = x + y
print("x + y : ", z)
z = x - y
print("x - y : ", z)
z = x * y
print("x * y : ", z)
z = x / y
print("x / y : ", z)

z = x % y
print("x % y : ", z)
z = x // y
print("x // y : ", z)

z = x ** y
print("x ** y : ", z)

str_x = "hello"
str_y = "python"

str_z = str_x + str_y
print("str_x + str_y:", str_z)

# unsupported operand type(s) for -: 'str' and 'str'
# str_z = str_x - str_y
# print("str_x + str_y:", str_z)

str_z = str_x * 2
print("str_x * 2", str_z)

delayed_effect_skill_ = "" # snake_case
delayedEffectSkillA = "" #camelCase

array_x = [3, 6]
array_y = [2, 5]

array_z = array_x + array_y
print("array_x + array_y :", array_z)
array_z = array_x * 2
print("array_x * 2 :", array_z)
array_z = array_x * array_y[0] # 해당 인덱스에 있는 요소가 정수형일 때
print("array_x + array_y :", array_z)

# 논리연산자
report_card = {
    "국어": 3,
    "수학": 2,
    "영어": 6,
    "물리": 4,
    "화학": 2,
    "생명과학": 5,
}

can_apply = report_card["국어"] < 3 and report_card["수학"] < 2 and report_card["영어"] < 3
print("지원가능여부 : ", can_apply)

# 3합 6
total_score = report_card["국어"] + report_card["수학"] + report_card["영어"] <= 6
print("3합 6 :", total_score )

# 과학 영재반
can_apply_class_for_the_gifted = report_card["물리"] == 1 or report_card["화학"] == 1 or report_card["생명과학"] == 1
print("영재반 지원가능여부 :", can_apply_class_for_the_gifted )