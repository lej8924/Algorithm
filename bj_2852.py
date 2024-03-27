import sys

n = int(sys.stdin.readline())
team1,team2 = 0,0
tmp1,tmp2 = 0,0
winner = 0

for _ in range(n):
    team,time = sys.stdin.readline().split(" ")
    min,sec = map(int,time.split(":"))
    time = 60 * min + sec
    
    # team1이 득접에 성공했을 때
    if team == '1':
        # 비기고 있는 상황일 때
        if winner == 0:
            winner += 1
            tmp1 = time
        # 비기는 상황이 아닐 때
        elif winner != 0:
            winner += 1
            # team1이 득점한 후 비기게 되었을 때
            if winner == 0:
                team2 += time - tmp2
    #team2가 득점에 성공했을 때
    else: 
        # 비기고 있는 상황일 때
        if winner == 0:
            winner -= 1
            tmp2 = time
        # 비기는 상황이 아니였을 때
        elif winner != 0:
            winner -= 1
            #team2가 득점한 후 비기게 되었을 때
            if winner == 0:
                team1 += time - tmp1
                
# 결과적으로 team1이 이겼을 때
# 끝나는 시간에서 직전까지의 득점 시간을 빼주어서 더해줌
if winner > 0:
    team1 += 60*48 - tmp1
# 결과적으로 team2가 이겼을 때
# 끝나는 시간에서 직전까지의 득점 시간을 빼주어서 더해줌
elif winner < 0:
    team2 += 60*48 - tmp2


print('{:0>2}:{:0>2}'.format((team1)//60,team1%60))
print('{:0>2}:{:0>2}'.format((team2)//60,team2%60))

