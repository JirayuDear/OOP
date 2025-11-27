def max(list):
    n = len(list)
    if n > 1:
        i = n-1
        max = 0
        a = i
        index = 0
        for _ in range(a):
            for _ in range(i):
                if(max <= int(list[index])*int(list[_+1+index])):
                    max = int(list[index])*int(list[_+1+index])
            index += 1
            i -= 1
        if max != 0:
            print(max)
        else:
            print("Invalid")
    else:
        print("Invalid")


list = input().strip('[]').split(',')
max(list)