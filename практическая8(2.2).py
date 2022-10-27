n=3
A=[]
for i in range(n):
    B=[]
    for j in range(n):
        B.append(int(input()))
    A.append(B)
for i in range(n):
    for j in range(n):
        print (A[i][j],end=' ')
    print()
for i in range(n):
    for j in range(n):
        a=A[0][0]
        A[0][0]=A[0][2]
        A[0][2]=a
        a=A[2][0]
        A[2][0]=A[2][2]
        A[2][2]=a
print('new matrix')
for i in range(n):
    for j in range(n):
        print(A[i][j],end=' ')
    print()
