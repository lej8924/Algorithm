import sys 
n = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))

people.sort()
answer = 0

for i in range(1,n+1):
    answer += sum(people[0:i])

print(answer)