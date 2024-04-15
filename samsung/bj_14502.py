from collections import deque
import copy 
n,m= map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    global cnt_0
    queue = deque([])
    board2 = copy.deepcopy(board)
    
    for i in range(n):
        for j in range(m):
            if board2[i][j] == 2:
                queue.append([i,j])
    

    while queue:
        r,c = queue.popleft()
        for k in range(4):
            nx = r + dx[k]
            ny = c + dy[k]
            if (0 <= nx < n) and (0 <= ny < m):
                if board2[nx][ny] == 0:
                    board2[nx][ny] = 2
                    queue.append([nx,ny])
    
    tmp_cnt = 0;
    for i in range(n):
        for j in range(m):
            if board2[i][j] == 0:
                tmp_cnt += 1
    
    cnt_0 = max(cnt_0,tmp_cnt)
    

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt+1)
                board[i][j] = 0

cnt_0 = 0
make_wall(0)
print(cnt_0)
                
                    