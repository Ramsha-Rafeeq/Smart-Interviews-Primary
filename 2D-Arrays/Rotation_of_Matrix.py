n=3
matrix=[[1,2,3],
        [8,9,4],
        [7,6,5]]
mat=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mat[j][n-1-i]=matrix[i][j]
for row in mat:
    print(*row)

#inplace traversal

for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    matrix[i].reverse()
for row in matrix:
    print(*row)