n = input('Enter the string ')

l = len(n)

for i in range(l):
    print(n[i])

print('')

st = n[-1::-1]

print(st)

print()
for k in range(-1,-l,-1):
    print(st[k])




