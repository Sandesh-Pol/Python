def  fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
    
def main():
    n = int(input('Enter the number : '))
    res = fact(n)
    print("Factorial of numbe is : ",res)
    
if __name__ == "__main__":
    main()