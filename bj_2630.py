n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]



def cut_half(x,y,n):
    global white,blue
    color = board[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != board[i][j]:
                cut_half(x, y, n // 2)        # 1사분면
                cut_half(x, y + n // 2, n // 2)      # 2사분면
                cut_half(x + n // 2, y, n // 2)      # 3사분면
                cut_half(x + n // 2, y + n // 2, n // 2)    # 4사분면
                return

    if color == 0:
        white += 1
    else:
        blue += 1
    
    
white,blue = 0,0
cut_half(0,0,n)
print(white)
print(blue)
    