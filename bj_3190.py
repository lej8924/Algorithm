import sys 
from collections import deque
board_n = int(sys.stdin.readline())
board = [[0 for _ in range(board_n)] for _ in range(board_n)]

apple_n = int(sys.stdin.readline())
for _ in range(apple_n):
    tmp = sys.stdin.readline().split()
    apple_x,apple_y = int(tmp[0]),int(tmp[1])
    board[apple_x-1][apple_y-1] = 2 # 사과 위치는 2로 표현함

# snake_n = int(sys.stdin.readline())
# snake_movings = []
# for _ in range(snake_n):
#     tmp = sys.stdin.readline().split()
#     tmp[0] = int(tmp[0])
#     snake_movings.append(tmp)
    
l = int(sys.stdin.readline())
times = [0]*10000
for _ in range(l):
    when, dir = sys.stdin.readline().split()
    times[int(when)] = dir
    
snake = [[0,0]]
snake_x , snake_y = 0,0
board[0][0] = 1
cnt = 0
# pointer = {0:[0,1],1:[-1,0],2:[0,-1],3:[1,0]}

# 위 오 아 왼 시계방향 혹은 반시계방향대로 차례대로 인덱스를 설정해야 함
dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = 1

while(True):
    cnt += 1
    
    snake_x += dx[direction]
    snake_y += dy[direction]
    
    if snake_x < 0 or snake_y < 0 or snake_x >= board_n or snake_y >= board_n or board[snake_x][snake_y] == 1:
        break
    
    # 사과를 만난다면?
    if board[snake_x][snake_y] == 2:
        snake.append([snake_x,snake_y])
        board[snake_x][snake_y] = 1
    
    # 그냥 비어있다면?
    elif board[snake_x][snake_y] == 0:
        snake.append([snake_x,snake_y])
        board[snake_x][snake_y] = 1
        
        delX,delY = snake.pop(0)
        board[delX][delY] = 0
    
    if ( times[cnt] == 'D'): # 방향 전환해야할 시간이면
        direction = ( direction+1 )%4
    elif ( times[cnt] == 'L'):
        direction = ( direction+3 )%4
        
print(cnt)