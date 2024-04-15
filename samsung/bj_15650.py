n,m = map(int,input().split())


arr = []
visited = [0] * (n+1)

def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return

    for i in range(1,n+1):
        if not visited[i]:
            if len(arr)==0:
                visited[i] = True
                arr.append(i)
                dfs()
                arr.pop()
                visited[i] = False
            elif len(arr) >= 1 and arr[-1] < i:
                visited[i] = True
                arr.append(i)
                dfs()
                arr.pop()
                visited[i] = False

dfs()