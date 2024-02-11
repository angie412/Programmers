n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
new_arr1 = []
new_arr2 = []
for i in range (len(arr1)) :
    bin_num = bin(arr1[i])[2:]
    new_arr1.append(bin_num)
for i in range (len(arr2)) :
    bin_num = bin(arr2[i])[2:]
    new_arr2.append(bin_num)

for j in range(len(new_arr1)):
    if len(new_arr1[j]) < n :
        length = n - len(new_arr1[j])
        multy = str(0)*length
        new_arr1[j] = multy+new_arr1[j]   

for j in range(len(new_arr2)):
    if len(new_arr2[j]) < n :
        length = n - len(new_arr2[j])
        multy = str(0) * length
        new_arr2[j] = multy+new_arr2[j] 

print(new_arr1)
print(new_arr2)
result = [] 
for i in range(len(new_arr1)) :
    row = []
    for j in range(len(new_arr2)):
        if new_arr1[i][j] == '1' or new_arr2[i][j] == '1' :
            row.append('#')
        else :
            row.append(' ')

    result.append(row)

answer = []
for row in result :
    answer.append(''.join(row))
# 위의 일차원 -> 이차원, 이차원->일차원 다시 보기 

