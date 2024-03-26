import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    arr.append(tmp)
    
arr = sorted(arr, key = lambda x : x[0])
solve = []
for deadline,cnt in arr:
    heapq.heappush(solve,cnt)
    if deadline == len(solve):
        if cnt <= solve[0]:
            continue
        heapq.heappop(solve)

print(sum(solve))