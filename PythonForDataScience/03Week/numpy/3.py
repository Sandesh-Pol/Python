L, W = map(int, input().split())
A = []
for _ in range(L):
    row = list(map(int, input().split()))
    A.append(row)
H = int(input())
ideal_row = -1
ideal_col = -1
for i in range(L - 1, -1, -1):
    for j in range(W):
        if H <= A[i][j]:
            ideal_row = i
            ideal_col = j
            break
    if ideal_row != -1:
        break
if ideal_row == -1:
    ideal_row = L - 1
    ideal_col = W - 1
print(ideal_row, ideal_col)
