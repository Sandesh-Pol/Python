def is_palindrome(n, original_n=None):
    if original_n is None:
        original_n = n

    if n == 0:
        return original_n == int(str(original_n)[::-1])
    
    else:
        last_digit = n % 10
        new_n = n // 10
        original_n = original_n * 10 + last_digit
        return is_palindrome(new_n, original_n)

number = int(input("Enter a number: "))
if is_palindrome(number):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")
