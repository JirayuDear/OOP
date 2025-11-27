def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day,month,year):
    try:
        day_of_years = 0
        day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        if day <= 0 or day > 31 or year <= 0 or month <= 0 or month > 12:
            return 'Invalid'
        if month == 2:
            if is_leap(year) and day > 29:
                return "Invalid"
            elif not is_leap(year) and day > 28:
                return "Invalid"
        elif month in [4, 6, 9, 11] and day > 30:
            return "Invalid"
        
        if is_leap(year):
            day_in_month[2] += 1
        else:
            if month == 2 and day == 29:
                return -1
        
        for i in range(1, month):
            day_of_years += day_in_month[i]
        day_of_years += day

        return day_of_years
    except IndexError:
        return 'Invalid'
try:
    date = input().split('-')
    date = [i.strip() for i in date]
    date[2] = int(date[2])
    isleap = is_leap(date[2])
    try:
        date = [int(i) for i in date]
        result = day_of_year(date[0],date[1],date[2])
    except:
        result = 'Invalid'
except:
    result = 'Invalid'
    isleap = 'Invalid'

print(f"day of year: {result} is_leap: {isleap}")