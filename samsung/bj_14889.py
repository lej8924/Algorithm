n = int(input())
arr = [list(map(int,input().split())) for _  in range(n)]
visited = [0 for _ in range(n)]
min_value = 1e4

def backtracking(depth,idx):
    global min_value
    if depth == n//2:
        #power1 : 스타트팀
        #power2 : 링크팀
        power1 ,power2 = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += arr[i][j]
        min_value = min(min_value,abs(power1-power2))
        return
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            backtracking(depth+1,i+1)
            visited[i] = False

backtracking(0,0)
print(min_value)
            