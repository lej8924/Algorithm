import math
n,m,k = map(int,input().split())
# board_m = [[0]*n for _ in range(n)]
# board_s = [[0]*n for _ in range(n)]
# board_d = [[[]]*n for _ in range(n)]

board = [[[] for _ in range(n)] for _ in range(n)]  

# visited = [[0]*n for _ in range(n)]

# fire = [list(map(int,input().split())) for _ in range(m)]
fireball = []
for _ in range(m):  
    r, c, m, s, d = map(int, input().split())  
    fireball.append((r-1, c-1, m,s,d))  
    
dxy = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

for _ in range(k):
    # nx, ny = 0, 0
    while fireball:
        r,c,m,s,d = fireball.pop()
        nx = (r + dxy[d][0] * s) % n
        ny = (c + dxy[d][1] * s) % n
        # print("어디에",nx,ny)
        # print("?/: ",m,s,d)
        board[nx][ny].append([m,s,d])

    
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:
                new_m,new_s = 0,0
                cnt_even = 0
                cnt_odd = 0
                length = len(board[i][j])
                while board[i][j]:
                    
                    m,s,d = board[i][j].pop()
                    # print(m,s,d)
                    new_m += m
                    new_s += s
                    # print("질량 속력",new_m,new_s)
                    if d % 2 ==0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                
                if cnt_even == length or cnt_odd == length:
                    # print("even")
                    nd = [0,2,4,6]
                elif new_m > 0:
                    nd = [1,3,5,7]
                    # print("odd")
                
                if new_m // 5:
                    for ddd in nd:    
                        fireball.append([i,j,new_m//5,new_s//length,ddd])
            elif len(board[i][j]) == 1:
                fireball.append([i,j] + board[i][j].pop())

                     


# res = 0              
# for i in range(n):
#     for j in range(n):
#         res += board[i][j][0]
        
# print(fireball)
print(sum(i[2] for i in fireball),end='')
    