import sys

n,m = map(int,sys.stdin.readline().split())

num_arr = list(map(int,sys.stdin.readline().split()))


def black_jack(n,m,num_arr):
    res = 0

    for i in range(n-2):
        if num_arr[i] > m:
            continue
        
        for j in range(i+1,n-1):
            if num_arr[i] + num_arr[j] > m:
                continue
            
            for k in range(j+1,n):
                tmp = num_arr[i] + num_arr[j] + num_arr[k]
                if tmp == m:
                    return m
                if tmp > res and tmp < m :
                    res = tmp

    return res

res = black_jack(n,m,num_arr)
print(res,end='')