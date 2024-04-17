num = int(input())
  
def test(num,object_num):
    res = 0
    num_sum = sum(list(map(int,str(num))))
    # print("num:",num)
    # print("num_sum:",num_sum)
    res = num + num_sum
    if object_num == res:
        return num
    else:
        return float("inf")
    
min_cons = float("inf")

for i in range(num):
    tmp = test(i,num)
    # print("tmp :",tmp)
    if min_cons > tmp:
        min_cons = i
        
if min_cons == float("inf"):
    print(0,end='')
else:
    print(min_cons,end='')
    