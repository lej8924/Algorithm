

def dfs(change):
    global answer
    if change == cnt:
        answer = max(answer,int("".join(map(str,arr))))
        return
    for i in range(1,length):
        for j in range(i+1,length):
            
            arr[i],arr[j] = arr[j],arr[i]
            tmp = int("".join(map(str,arr)))
            
            if not [change,tmp] in visited:
                dfs(change+1)
                visited.append([change,tmp])
            arr[j],arr[i] = arr[i],arr[j]


n = int(input())

for i in range(n):
    num, cnt = input().split()
    arr = list(num)
    answer = 0
    length = len(arr)
    visited = []
    dfs(0)
    print(f'#{i+1} {answer}')