arr = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    tmp = list(map(int,input().split()))
    arr[i] = tmp


max_res = -1
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max_res:
            max_res = arr[i][j]
            max_row = i + 1
            max_col = j + 1

print(max_res)
print(max_row,max_col, end='')