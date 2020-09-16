print("Enter a square matrix as input")
print("Enter N")
n=int(input())
mat=[]
for i in range(0,n):
    mat.append([int(x) for x in input().split()])
for i in range(0,int(n/2)):
    for j in range(i,n-i-1):  # i in range 0 to n/2 and j in range between i,n-i-1 because we are swapping one whole phase of the matrix in each iteration
        #The following lines are used to swap the array elements over 90 deg in place
        #Observe closely how right hand side expression differs from left hand side by Ri=(n-1-Lj) and Rj=Li
        t1=mat[i][j]
        mat[i][j]=mat[j][n-i-1]
        mat[j][n-i-1]=mat[n-i-1][n-j-1]
        mat[n-1-i][n-j-1]=mat[n-1-j][i]
        mat[n-1-j][i]=t1
for i in range(0,n):
    for j in range(0,len(mat[0])):
        print(mat[i][j],end=" ")
    print()
    
        
    
