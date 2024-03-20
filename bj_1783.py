import sys

n,m = map(int,sys.stdin.readline().split())

res = 0
if n == 1:
    res = 1
elif n == 2:
    if m >= 1 and m <= 6:
        res = (m+1)//2 
    elif m >= 7:
        res = 4
elif n >= 3:
    if m <= 6:
        res = min(m,4)
    elif m >= 7:
        res = m - 2
        
print(res)