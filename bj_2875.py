import sys
import math
# N,M,K=map(int,sys.stdin.readline().split())


# teams=min(N//2,M)


# tmp_N=N-2*teams
# tmp_M=M-teams


# remain=tmp_M+tmp_N
# if remain>=K:
#     print(teams)
    
# else:
#     K=K-remain

#     teams=teams-math.ceil(K/3)
#     if teams<=0:
#         teams=0
    
#     print(teams)
    
#################################################3
import sys

N,M,K = map(int,sys.stdin.readline().split())

teams = min(N//2,M)

while(True):
    tmp_N = N - 2 * teams
    tmp_M = M - teams
    sum = tmp_M + tmp_N
    
    if sum >= K:
        print(teams)
        break
    else:
        teams -= 1
        tmp_N += 2
        tmp_M += 1
        if teams == 0:
            print(teams)
            break