f = int(input("f : "))
u = int(input("u : "))
o = int(input("o : "))
n = int(input("n : "))

print(bin(f))
print(bin(u))
print(bin(o))
print(bin(n))

t = f + u 

u = u - o

u = u + n

res = t - u


print(bin(res))