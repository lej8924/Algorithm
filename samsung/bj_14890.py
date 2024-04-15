import math
n, l = map(int,input().split())
loadmap = [list(map(int,input().split())) for _ in range(n)]

def check_line(arr):
    used = [False for _ in range(n)]
    
    for i in range(1,n):
        # 칸의 높이 차이는 1이어야 한다.
        if abs(arr[i] - arr[i-1]) > 1:
            return False
        
        # 높 -> 낮
        if arr[i-1] > arr[i] :
            for j in range(l):
                # 칸이 오버되거나 이미 설치되었거나 낮은 곳의 높이가 다르다면
                if (i+j) >= n or used[i+j] or arr[i] != arr[i+j]:
                    return False
                if arr[i] == arr[i+j]:
                    used[i+j] = True
        
        # 낮 -> 높
        elif arr[i-1] < arr[i] :
            for j in range(l):
                # 칸이 오버되거나 이미 설치되었거나 낮은 곳의 높이가 다르다면
                if (i-j-1) < 0 or used[i-j-1] or arr[i-1] != arr[i-j-1]:
                    return False
                if arr[i-1] == arr[i-j-1]:
                    used[i-j-1] = True
    return True

res = 0
# 행별로
for tmp in loadmap:
    if check_line(tmp):
        res += 1
    
# 열별로
for i in range(n):
    if check_line([loadmap[j][i] for j in range(n)]):
        res += 1

print(res)

            