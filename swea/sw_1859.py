t = int(input())
cases = []
for tt in range(t):
    case_n = int(input())
    case = list(map(int,input().split()))
    
    max_cost = case[case_n-1]
    res =  0
    cnt = 0
    for i in range(case_n-2,-1,-1):
        if max_cost > case[i]:

            res += max_cost - case[i]

        elif max_cost < case[i]:

            max_cost = case[i]
    print(f'#{tt+1} {res}')
            
    
