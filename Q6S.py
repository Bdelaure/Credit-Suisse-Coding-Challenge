import math as m
words = "its harder to read code than to write it"
#words = "coding"
words = words.replace(" ","")
length = len(words)
length_sqrt = m.sqrt(length)
ceiling = int(max(length_sqrt + 1,m.ceil(length_sqrt)))
flor = int(m.floor(length_sqrt))

poss_range = list(range(flor,ceiling+1))
matrix_param = []

for i in range(len(poss_range)):
    for j in range(len(poss_range)):
        if poss_range[i] <= poss_range[j] and poss_range[i] * poss_range[j] >= length:
            matrix_param.append((poss_range[i],poss_range[j],poss_range[i] * poss_range[j]))

matrix_param.sort(key=lambda item:item[2])

row = matrix_param[0][0]
col = matrix_param[0][1]
counter = 0

matrix = [[""] * row for j in range(col) ]
for j in range(col):
    for i in range(row):
        if i != 0 or j != 0:
            counter = counter + 1
        if counter == length:
            break
        matrix[j][i] = words[counter]


print(flor)
print(ceiling)
print(poss_range)
print(matrix_param)
print(matrix)
print(counter)
print(length)