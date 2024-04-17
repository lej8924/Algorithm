

n1,m1 = map(int,input().split())
mat1 = [list(map(int, input().split())) for _ in range(n1)]

n2,m2 = map(int,input().split())
mat2 = [list(map(int, input().split())) for _ in range(n2)]

res = [[0 for _ in range(m2)] for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        for k in range(m1):
            res[i][j] += mat1[i][k] * mat2[k][j]

for tmp in res:
    print(*tmp)