n,m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
res = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,total,cnt):
    global res
    if cnt == 3:
        res = max(total,res)
        return
    
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n  and 0 <= ny < m and visited[nx][ny] == 0:
            # 뻑큐 모양을 구현하기 위해
            # 자기 자신으로 다시 돌아가서 구하면 가능
            if cnt == 1:
                visited[nx][ny] = 1
                dfs(i,j,total + paper[nx][ny],cnt + 1)
                visited[nx][ny] = 0
                
            visited[nx][ny] = 1
            dfs(nx,ny,total + paper[nx][ny],cnt + 1)
            visited[nx][ny] = 0
            
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,paper[i][j],0)
        visited[i][j] = 0
print(res)
        