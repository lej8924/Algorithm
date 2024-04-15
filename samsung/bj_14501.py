N = int(input())

dp = [0] * (N+1)
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(N-1,-1,-1):
    if i + arr[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1] , dp[i+arr[i][0]] + arr[i][1])

print(dp[0],end='')
    
    