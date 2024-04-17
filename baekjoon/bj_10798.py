import sys

arr = [0 for _ in range(5)]

for i in range(5):
    arr[i] = sys.stdin.readline().strip()


for i in range(15): 
  for j in range(5): 
    if i < len(arr[j]):
      print(arr[j][i], end="")


    