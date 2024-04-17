import sys
input = sys.stdin.readline
print = sys.stdout.write

num = int(input())

for i in range(1,num+1): # 1,2,3,4,5
    for t1 in range(num-i):
        print(" ")
    for t2 in range(i*2-1):
        print('*')
    # for t3 in range(num-i):
    #     print(" ")
    print("\n")
    
    
for i in range(num-1,0,-1): # 4,3,2,1

    for t1 in range(num-i):
        print(" ")
    for t2 in range(i*2-1):
        print('*')
    # for t3 in range(num-i):
    #     print(" ")
    if i == 1:
        break
    print("\n")
    