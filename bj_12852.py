n = int(input())

dp = [0 for _ in range(n+1)]
history = [0 for _ in range(n+1)]

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    history[i] = i - 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
        history[i] = i//2
    if i % 3 ==0:
        dp[i] = min(dp[i],dp[i//3]+1)
        history[i] = i//3

print(dp[n])
print(n,end=' ')

back_num = n
while history[back_num] != 0:
    print(history[back_num], end=" ")
    back_num = history[back_num]