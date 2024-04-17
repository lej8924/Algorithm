import sys
input = sys.stdin.readline
print = sys.stdout.write

origin = [1,1,2,2,2,8]

arr = list(map(int,input().split()))

res = []

for i in range(len(arr)):
    if origin[i] != arr[i]:
        res.append(origin[i]-arr[i])
    else:
        res.append(0)
        
for i in range(len(res)):
    print(str(res[i])+" ")