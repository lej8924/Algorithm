
def cut_nine(x,y,n):
    global x1,x2,x3
    number = mat[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if number != mat[i][j]:
                cut_nine(x,y,n//3)
                cut_nine(x,y+n//3,n//3)
                cut_nine(x,y+(n//3)*2,n//3)
                
                cut_nine(x+n//3,y,n//3)
                cut_nine(x+n//3,y+n//3,n//3)
                cut_nine(x+n//3,y+(n//3)*2,n//3)
                
                cut_nine(x+(n//3)*2,y,n//3)
                cut_nine(x+(n//3)*2,y+n//3,n//3)
                cut_nine(x+(n//3)*2,y+(n//3)*2,n//3)
                return
    
    result[number] +=1 


n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
result = {-1:0, 0:0,1:0}
cut_nine(0,0,n)
for i in result.values():
    print(i)