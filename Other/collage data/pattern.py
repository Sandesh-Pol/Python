num_rows = 15

start_num = 1

for i in range(num_rows):
    for j in range(i + 1):
        print(start_num, end=" ")
        start_num += 1
    print()
