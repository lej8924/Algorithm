#최소 힙
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0 and len(heap) > 0:
        print(heapq.heappop(heap))
    elif len(heap) == 0 and m == 0:
        print(0)
    else:
        heapq.heappush(heap,m)
    