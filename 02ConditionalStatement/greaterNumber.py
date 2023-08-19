a = int(input('Enter the number : '))
b = int(input('Enter the number : '))
c = int(input('Enter the number : '))

res = a if (a > b and a > c) else (b if b > c else c)

print(res)

print(a,b,c)

print(id(a),id(b))