#  Write a Python Program to check if a string is palindrome 
# or not.


str1 = input("Enter the string : ")

str2 = str1[::-1]
print(str1[0::-1])

if str1 == str2:
    print('String is palindrome!')
else:
    print("String is not palindrome!")
