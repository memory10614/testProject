arr = ['AA','BB','CC','DD']

for i in arr:
    print(i)


#수학
test = [{ 'answer' : [1, 3, 4, 5, 3, 1, 2, 3, 4]},
{ 'answer' : [1, 2, 4, 5, 5, 1, 2, 3, 3]},
{ 'answer' : [1, 4, 4, 1, 3, 1, 2, 3, 4]},
{ 'answer' : [2, 5, 4, 5, 3, 1, 1, 3, 4]},
{ 'answer' : [1, 3, 3, 5, 3, 1, 3, 5, 4]},
{ 'answer' : [4, 3, 2, 5, 2, 1, 5, 3, 4]},
{ 'answer' : [1, 3, 5, 5, 3, 1, 2, 3, 1]}]

a =                [1, 5, 2, 4, 5, 2, 3, 4]
correct_answer =   [1, 3, 2, 4, 5, 3, 1, 2, 3, 4]

# 학생의 점수 구하기 한 문항당 10점이라 가정.

for (student, correct) in zip(a,correct_answer):
    print(student , '/', correct)