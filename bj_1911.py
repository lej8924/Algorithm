import sys 
import math
## 물웅덩이는 겹치지 않는다
## 널빤지의 크기와 물웅덩이끼리의 거리에 따라서 널빤지가 이어질 수도 있다

n,l = map(int,sys.stdin.readline().split())
holes = []

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split(" "))
    holes.append([a,b])

holes.sort(key=lambda x :x[0])

point = holes[0][0]

cnt = 0
for hole in holes:
    if point > hole[1]: # point가 구멍의 끝보다 크다면 패스
        continue
    
    elif point < hole[0]: # point가 구멍의 시작보다 작다면
        point = hole[0] # 시작위치로 point를 옮김
        
    dist = hole[1] - point # dist는 끝 - point의 위치를 해줌
    r = 1 # 만약 웅덩이의 거리가 널빤지의 거리로 나눠떨어지지 않는다면?
    if dist % l == 0: # 나눠떨어진다면?
        r = 0
    count = dist//l + r # 거리에서 널빤지의 거리만큼 나눠주고 0혹은 1을 더해줌
    point += count * l # point는 널빤지를 깔아준만큼 이동함
    cnt += count # count가 사용한 널빤지의 개수이므로 더해줌
    
print(cnt,end='') # 결과출력