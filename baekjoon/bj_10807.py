import sys
input = sys.stdin.readline
print = sys.stdout.write


N = int(input())

cnt = 0
arr = list(map(int,input().split()))

num = int(input())


for i in range(len(arr)):
    if arr[i] == num:
        cnt += 1

print(str(cnt))

