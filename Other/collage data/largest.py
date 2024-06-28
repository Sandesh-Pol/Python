def acceptNumbers():
    l = []
    num = int(input('Enter the number of input values: '))
    for i in range(num):
        n = int(input(f"Enter element {i}: "))
        l.append(n)
    return l

numbers = acceptNumbers()
numbers.sort()  
largest = numbers[-1]  
smallest = numbers[0] 

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
