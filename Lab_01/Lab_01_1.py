def calculate_sum(num):
    check = num
    check = int(check)
    if 0<=check<=9:
        two = int(num + num)
        three = int(num + num + num)
        four = int(num + num + num + num)
        num = int(num)
        all_sum = num + two + three + four
        print(all_sum)
    else:
        print("Invalid")

num = input()
calculate_sum(num)
