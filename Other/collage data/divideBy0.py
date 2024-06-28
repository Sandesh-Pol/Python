try:
    a = int(input("Enter the Divident : "))
    b = int(input("Enter the Divisior : "))

    res = b // a

except ZeroDivisionError as e:
    print(e)
