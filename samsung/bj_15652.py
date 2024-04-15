n,m = map(int,input().split())

arr = []
visited = []

def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return

    for i in range(1,n+1):
        if len(arr) == 0:
            arr.append(i)
            dfs()
            arr.pop()
        elif len(arr) >= 1 and arr[-1] <= i:
            arr.append(i)
            dfs()
            arr.pop()
            
dfs()