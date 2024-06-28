## Simple approch

# def fact(num):
#     factors = [i for i in range(1, num + 1) if num % i == 0]
#     return factors

# def gcd(*args):
#     if len(args) < 2:
#         print("At least two numbers are required for GCD calculation.")
#         return
    
#     common_factors = set(fact(args[0]))
    
#     for num in args[1:]:
#         common_factors &= set(fact(num))

#     if not common_factors:
#         print("No common factors found.")
#     else:
#         greatest_common_factor = max(common_factors)
#         print("Greatest common factor is:", greatest_common_factor)

# gcd(100,50)



# new approch

# def gcd(m,n):
#     cf = []
#     for i in range(1,min(m,n)+1):
#         if (m%i==0 and n%i==0):
#             cf.append(i);
#     return(cf[-1])

# print(gcd(5,10))





#more simple

# def gcd(m,n):
#     for i in range(1,min(m,n)+1):
#         if (m%i==0 and n%i==0):
#             res = i
#     return(res)





# def gcd(m,n):
#     i = min(m,n)

#     while i>0:
#         if m%i ==0 and n%i ==0:
#             return i
#     else:
#         i = i-1





# recurtion angrothem 

# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     if (m%n)==0:
#         return(n)
#     else:
#         diff = m-n
#         return(gcd((n,diff),min(n,diff)))

# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     if (m%n)==0:
#         return(n)
#     else:
#         diff = m-n
#         return(gcd(n,m%n))

def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while (m%n) != 0:
        (m,n) = (n,m%n)
    return n 
    
print(gcd(5,5))





