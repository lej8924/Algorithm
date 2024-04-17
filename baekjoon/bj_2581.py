import sys 
import math

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0 :
            return False
    return True

prime_arr = []
for tmp in range(a,b+1):
    if is_prime(tmp) and tmp != 1:
        prime_arr.append(tmp)

if len(prime_arr) ==0 :
    print(-1,end='')
else:
    print(sum(prime_arr))
    print(min(prime_arr),end='')