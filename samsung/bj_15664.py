n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
visited = [0] * n
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str,tmp)))
        return
    check = 0
    for i in range(n):
        if len(tmp) == 0 and check != arr[i]:
            tmp.append(arr[i])
            visited[i] = True
            check = arr[i]
            dfs()
            tmp.pop()
            visited[i] = False
        elif len(tmp) >= 1 and not visited[i] and tmp[-1] <= arr[i] and check != arr[i] :
            visited[i] = True
            tmp.append(arr[i])
            check = arr[i]
            dfs()
            tmp.pop()
            visited[i] = False

dfs()