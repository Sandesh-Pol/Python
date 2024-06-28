def print_pattern():

    n = 7 

    for i in range(0, n//2 + 1):

        for j in range(i):

            print(" ", end="")
        
        for k in range(n - 2 * i):

            if k % 2 == 0:

                print("1", end="")

            else:
                
                print("0", end="")
        
        print()

print_pattern()
