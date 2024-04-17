import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    tmp = []
    for i in range(1,n):
        if n % i ==0:
            tmp.append(i)
    if sum(tmp) == n:
        div = ' + '.join(map(str, tmp))
        print(f'{n} = {div}')
    else:
        print(f"{n} is NOT perfect.")

                
                
