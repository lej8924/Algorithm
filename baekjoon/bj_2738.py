
tmp = list(map(int,input().split()))
N,M = tmp[0],tmp[1]

A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int,input().split()))
    
for i in range(N):
    B[i] = list(map(int,input().split()))
    

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()

