N = int(input())   
list = []

for n in range(N):
    command = input().split()

    if len(command) == 1:
        if command[0] == "print":
            eval(command[0] + "(list)")
        else:
            eval("list." + command[0] + "()")

    elif len(command) == 2:
        eval("list." + command[0] + "(" + command[1] + ")")

    else:   
        eval("list." + command[0] + "(" + command[1] + ", " + command[2] + ")")