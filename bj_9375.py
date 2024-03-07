#패션왕 신해빈
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    tmp = {}
    for _ in range(m):
        a,b = sys.stdin.readline().strip().split(" ")
        if b in tmp.keys():
            tmp[b].append(a)
        else:
            tmp[b] = [a]
    cnt = 1
    for k in tmp:
        cnt *= len(tmp[k]) + 1
    print(cnt-1)
        
                
          
