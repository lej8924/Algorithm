def cut_four(x,y,n):
    global res
    color = board[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != board[i][j]:
                res += "("
                cut_four(x, y, n // 2) # 1사분면
                
                cut_four(x, y + n // 2, n // 2)      # 2사분면
                
                cut_four(x + n // 2, y, n // 2)      # 3사분면
               
                cut_four(x + n // 2, y + n // 2, n // 2)    # 4사분면
           
                res += ")"
                return None

    if color == 0 :
        res += '0'
    else:
        res += '1'
    return None

n = int(input())
board = [list(map(int,input())) for _ in range(n)]
res = ""
# tmp = []
cut_four(0,0,n)


print(res)

