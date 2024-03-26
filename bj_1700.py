import sys,copy
from collections import Counter

n,k = map(int, sys.stdin.readline().split())
devices = list(map(int, sys.stdin.readline().split()))

tap  = []
ans = 0

for idx,device in enumerate(devices):
    # 꼽으려는 기기가 이미 꽂혀있다면?
    if device in tap:
        continue
    # 멀티탭의 자리가 비어있다면?
    elif len(tap) < n:
        tap.append(device)
    # 둘 다 아니고 무언가를 뽑아주어야 한다면?
    # 현재 멀티탭에 있는 기기 중 가장 나중에 쓰이는 기기를 먼저 뽑아주어야 함
    else:
        ans += 1 # 뽑아주어야 하므로 ans에 1을 더해줌
        # 가장 나중에 쓰일 기기를 찾아주는 과정 
        tmp = devices[idx:]
        removed_idx = -1 # 삭제될 기기의 추후에 나오는 index(값이 클수록 삭제됨)
        removed_item = -1 # 삭제될 기기의 이름
        
        for x in tap:
            if x in tmp: # 만약 뒤에 나온다면?
                if removed_idx < tmp.index(x): 
                    removed_idx = tmp.index(x)
                    removed_item = x
            else: # 뒤에 나오지 않는다면?
                removed_item = x
                break
        
        tap[tap.index(removed_item)] = device

print(ans)
                
