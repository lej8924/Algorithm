n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]

dxy = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

dup = [[1,1],[-1,-1],[1,-1],[-1,1]]

clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for d,s in moves:
    dx,dy = dxy[d-1]
    moved_clouds = []
    visited = [[0]*n for _ in range(n)]
    for cloud1,cloud2 in clouds:
        cloud1 = (cloud1 + s*dx) % n
        cloud2 = (cloud2 + s*dy) % n
        
        board[cloud1][cloud2] += 1
        visited[cloud1][cloud2] = True
        moved_clouds.append([cloud1,cloud2])
    
    for cloud1,cloud2 in moved_clouds:
        
        for d1,d2 in dup:
            nx = cloud1 + d1
            ny = cloud2 + d2
            if nx >= n or ny >=n or nx < 0 or ny < 0:
                continue
            elif board[nx][ny] > 0:
                board[cloud1][cloud2] += 1
        
    new_clouds = []

    for i in range(n):
        for j in range(n):
            if visited[i][j]==True or board[i][j] < 2:
                continue
            
            new_clouds.append([i,j])
            board[i][j] -= 2
        
    clouds = new_clouds

res = 0
for i in range(n):
    for j in range(n):
        res += board[i][j]

print(res)
    
    
    
    

