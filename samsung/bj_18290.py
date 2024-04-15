n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

max_val = float('-inf')
# 우 좌 하 상


def dfs(x,y,idx,sum_val):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    global max_val
    if idx == k:
        max_val = max(max_val,sum_val)
        return
    
    for i in range(x,n):
        for j in range(y if i == x else 0,m):
            if visited[i][j]:
                continue
            
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    break
            
            else:
                visited[i][j] = True
                dfs(x,y,idx+1,sum_val+board[i][j])
                visited[i][j] = False
            
            
dfs(0,0,0,0)
print(max_val,end='')
        