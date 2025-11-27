def palindrome(num):
    if num.isdigit():
        max_palindrome = 0
        count = 0
        if num == "2":
            for i in range(99, 0, -1):
                for j in range(99, 0, -1):
                    if (i*j) >= max_palindrome:
                        check = str(i*j)
                        lenght = len(check)
                        for _ in range(len(check)):
                            if check[_] == check[lenght-1]:
                                count += 1
                                lenght -= 1
                        if count == len(check):
                            count = 0
                            max_palindrome = int(i*j)
                        else:
                            count = 0
            print(max_palindrome)               
        elif num == "3":
            for i in range(999, 0, -1):
                for j in range(999, 0, -1):
                    if (i*j) >= max_palindrome:
                        check = str(i*j)
                        lenght = len(check)
                        for _ in range(len(check)):
                            if check[_] == check[lenght-1]:
                                count += 1
                                lenght -= 1
                        if count == len(check):
                            count = 0
                            max_palindrome = int(i*j)
                        else:
                            count = 0 
            print(max_palindrome)
        else:
            print("Invalid")
    else:
        print("Invalid")

num = input()
palindrome(num) 