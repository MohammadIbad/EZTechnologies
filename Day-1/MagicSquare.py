n=int(input("Enter the Size of the Matrix:"))
matrix=[[0 for i in range(n)]for i in range(n)]
i=0
j=n//2
num=1
while num<=n*n:
    matrix[i][j]=num
    num=num+1
    newi=(i-1)%n
    newj=(j+1)%n
    if matrix[newi][newj]!=0:
        i=(i+1)%n
    else:
        i=newi
        j=newj
print(matrix)
