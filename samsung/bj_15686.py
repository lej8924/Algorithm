from itertools import combinations
n,m = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(n)]
chicken, house, val = [],[],[]

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])
            
dist_min = 1e9
visited = [0] * len(chicken)
def backtracking(idx,cnt):
    global dist_min
    
    if cnt == m:
        ans = 0
        for h in house:
            dist = 1e9
            for j in range(len(visited)):
                if visited[j]:
                    tmp = abs(h[0]-chicken[j][0]) + abs(h[1]-chicken[j][1])
                    dist = min(dist,tmp)
            ans += dist
        dist_min = min(ans,dist_min)
    
    for i in range(idx,len(chicken)):
        if not visited[i]:
            visited[i] = True
            backtracking(i+1,cnt+1)
            visited[i] = False

backtracking(0,0)
print(dist_min)

# result = 0
# for chi in combinations(chicken,m):
#     temp = 0
#     for h in house:
#         chi_len = 1e9
#         for j in range(m):
#             chi_len = min(chi_len,abs(h[0]-chi[j][0])+abs(h[1]-chi[j][1]))
#         temp += chi_len
#     result = min(result,temp)