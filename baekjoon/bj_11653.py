import sys

num = int(sys.stdin.readline())

d = 2
while d <= num:
    if num % d == 0:
        print(d)
        num = num / d
    else:
        d = d + 1
