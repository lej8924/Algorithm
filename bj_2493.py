import sys
n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
st = []
res = []
for i in range(n):
    while st:
        if st[-1][1] > tops[i]: # 수신이 가능한 상황
            res.append(st[-1][0]+1)
            break
        else: # 자신보다 낮으면 pop으로 빼냄 이러면 뒤의 탑에서도 유용함
            st.pop()
    if not st:
        res.append(0)
    st.append([i,tops[i]])
        
print(*res)