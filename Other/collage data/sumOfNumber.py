# Write a Python program to calculate sum of digit of given 
# number using function.


n = int(input("Enter the number : "))
total_sum = 0  # Initialize sum to 0

while n != 0:
    n1 = n % 10
    total_sum = total_sum + n1 % 10
    n //= 10

print("Sum of digits:", total_sum)


def sum_of_digits(number):
    digits = str(number)
    total_sum = 0
    for digit in digits:
        total_sum += int(digit)
    return total_sum

def input_number():
    return int(input("Enter a number: "))

def main():
    number = input_number()
    # Calculate the sum of digits using the function
    result = sum_of_digits(number)
    print("Sum of digits:", result)

if __name__ == "__main__":
    main()
