from collections import deque

n,k = map(int,input().split())

belt = deque(list(map(int,input().split())))
robot = deque([0 for _ in range(n)])

# cnt0 = 0 # 0의 개수를 세는 변수
step = 0 # 몇번째 단계인지 카운드

def check_belt(belt):
    cnt0 = 0
    for bb in belt:
        if bb == 0:
            cnt0 += 1
    return cnt0
    
            
while(True):
    step += 1
    # 1단계
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    # 2단계
    for i in range(n-2,-1,-1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            
    robot[n-1] = 0
    
    # 3단계 
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        
    # 4단계
    if check_belt(belt) >= k:
        break

    
print(step,end='')
    


       
            