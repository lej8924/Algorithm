from itertools import combinations
n,m = map(int,input().split())
# arr = [ 1+i for i in range(n+1)]

# for i in combinations(arr,m):
#     print(*i)
arr = []
visited = [0] * (n+1)
def backtracking():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            backtracking()
            arr.pop()
            visited[i] = False

backtracking()