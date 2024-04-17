
for t in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    res = 0
    for i in range(2,n-2):
        max_height = max(arr[i-2],arr[i-1],arr[i+1],arr[i+2])
        if max_height >= arr[i]:
            continue
        elif max_height < arr[i]:
            res += arr[i] - max_height
    
    print(f'#{t+1} {res}')