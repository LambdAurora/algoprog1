# 1. For what values the variable n is the expression n % 2 null?
#   If n is a multiple of 2.

# Write a function is_even which, from an integer n, returns True if n is even, else False.
def is_even(n):
    return n % 2 == 0


# In a year there is 365 days, except for leap year which have 366 days. Leap years are years that are divisible by 400 or divisible by 4 but no by 100.
def is_leep_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# Write a function get_number_of_days_in_month which, from two integers year and month return the number of days in the specified month.
def get_number_of_days_in_month(month, year):
    if (month <= 7 and month % 2 != 0) or (month > 7 and month % 2 == 0):
        return 31
    elif month == 2:
        if is_leep_year(year):
            return 29
        return 28
    return 30


print("is_even(5) = " + str(is_even(5)))
print("is_even(490) = " + str(is_even(490)))
print("is_leep_year(2019) = " + str(is_leep_year(2019)))
print("is_leep_year(2020) = " + str(is_leep_year(2020)))
print("is_leep_year(1900) = " + str(is_leep_year(1900)))
print("is_leep_year(2000) = " + str(is_leep_year(2000)))
print("get_number_of_days_in_month(2, 2020) = " + str(get_number_of_days_in_month(2, 2020)))
print("get_number_of_days_in_month(9, 2019) = " + str(get_number_of_days_in_month(9, 2019)))
print("get_number_of_days_in_month(2, 1900) = " + str(get_number_of_days_in_month(2, 1900)))
print("get_number_of_days_in_month(8, 2049) = " + str(get_number_of_days_in_month(8, 2049)))

