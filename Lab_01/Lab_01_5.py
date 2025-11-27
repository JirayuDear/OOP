def sort(nums):
    for n in num:
        if not n.isdigit() or len(num) < 0 or len(num) > 10 or len(num) == 1:
            print("Invalid")
            return
        else:
            num.sort()
            if num[0] == "0":
                for i in range(1, len(num)):
                    if num[i] != "0":
                        num[0], num[i] = num[i], num[0]
                        break
    print("".join(num))



num = input("").split()
sort(num)