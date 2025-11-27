day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 
        day_in_month[2] = 29 
        return True
    else: 
        day_in_month[2] = 28
        return False
def day_of_year(day, month, year, day2, month2, year2):
    if year <= 0 or month <= 0 or month > 12 or day <=0 or day > 31 or year2 <= 0 or month2 <= 0 or month2 > 12 or day2 <=0 or day2 > 31:
        return "Invalid"
    if month == 2 or month2 == 2:
        if is_leap(year) and day > 29:
            return "Invalid"
        elif not is_leap(year) and day > 28:
            return "Invalid"
        if is_leap(year2) and day2 > 29:
            return "Invalid"
        elif not is_leap(year2) and day2 > 28:
            return "Invalid"
    elif month in [4, 6, 9, 11] and day > 30:
        return "Invalid"
    if month2 in [4, 6, 9, 11] and day > 30:
        return "Invalid"

    sum_day = 0
    is_leap(year)
    if date[0] == date[1]:
        return 1
    if date[0] != date[1] and month != month2:
        sum_day += day_in_month[month] - day+1
        month += 1
    if month >= 12:
        month = 1
        year += 1
        day = 1
    for i in range(year2-year):
        is_leap(year)
        if year2 > year:
            for i in range(month,13):
                sum_day += day_in_month[i]
            year += 1
            month = 1
    if year == year2:
        is_leap(year)
        for i in range(month,month2):
            sum_day += day_in_month[i]
        sum_day += day2

    return sum_day

try:
    date = input().split(',')
    date = [i.split('-') for i in date]
    for i in range(len(date)):
        date[i] = [int(j.strip()) for j in date[i]]
    result = day_of_year(date[0][0], date[0][1], date[0][2], date[1][0], date[1][1], date[1][2])
    print(result)
except:
    print('Invalid')
    

