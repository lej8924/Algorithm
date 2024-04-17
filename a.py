num_list = [
 [3, 15, 8, 12, 7],
 [10, 5, 18, 2, 20],
 [9, 14, 6, 19, 1],
 [4, 11, 17, 13, 16],
 [7, 20, 5, 3, 18]
]

result1 = 0
result2 = []

for i in range(5):
    temp = 0
    for j in range(5):
        if i == j:
            result1 += num_list[i][j]
        temp += num_list[j][i]
    result2.append(temp)
    
print(result1)
print(result2)