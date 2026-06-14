def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    leap_year = True
    divisible_4 = year % 4
    divisible_100 = year % 100
    divisible_400 = year % 400

    if divisible_4 == 0 and divisible_100 != 0 or divisible_400 == 0:
        return leap_year
    else:
        return not leap_year
