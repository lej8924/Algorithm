import sys
n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
st = []
res = []
for i in range(n):
    while st:
        if st[-1][1] > tops[i]:
            res.append(st[-1][0]+1)
            break
        else:
            st.pop()
    if not st:
        res.append(0)
    st.append([i,tops[i]])
        
print(*res)