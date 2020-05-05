# Python Program to give transpose of the matrix

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

result = [[X[j][i] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
