# year = int(input('Enter the Year : '))

# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year") 

from numpy import False_, True_


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and (year%100!=0 or year%400==0):
        leap = True_
    else:
        leap = False_
    return leap

year = int(input())
print(is_leap(year))