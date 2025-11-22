print("피보나치 수열")
list = [1,1]

while list[-1] < input_number:
    print(list[-1])
    list.append(list[-1] + list[-2])