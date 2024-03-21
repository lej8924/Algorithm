import sys

n = int(sys.stdin.readline())
arr = []
alls = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    # print(tmp)
    arr.append(tmp)
    alls += tmp[1]

arr = sorted(arr,key = lambda x : x[0])

res = 0
for x in arr:
    res += x[1]
    if res >= alls/2:
        print(x[0])
        break