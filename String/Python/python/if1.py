a=int(input("Enter the number : "))
b=int(input("Enter second number : "))
c=int(input("Enter last number : "))
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)
    