n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

tmp = []
visited = [0]* len(arr)

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str,tmp)))
        return
    
    check = 0 # 숫자가 중복할 시에는 재귀를 돌지 말아야 하므로 이전 숫자를 기억해놓는다
    
    for i in range(len(arr)):
        if not visited[i] and check != arr[i]:
            visited[i] = True
            tmp.append(arr[i])
            check = arr[i]
            dfs()
            tmp.pop()
            visited[i] = False

dfs()