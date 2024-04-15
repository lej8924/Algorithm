import math
n = int(input())
exams = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = n
for exam in exams:
    exam -= b
    if exam > 0:
        cnt += math.ceil(exam/c)

print(cnt)