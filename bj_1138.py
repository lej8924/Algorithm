import sys

n = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().split()))
res = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        # res 리스트가 0이고, 앞에 필요한 사람 수와 같아질 경우
        if cnt ==  line[i] and res[j] == 0:
            res[j] = i + 1
            break
        # res가 그냥 0인 경우엔 본인보다 큰 사람의 자리를 만들어주어야 한다
        elif res[j] == 0:
            cnt += 1

print(" ".join(map(str,res)))
            
    
    