n=3
A=[]
for i in range(n):
    B=[]
    for j in range(n):
        B.append(int(input()))
    A.append(B)
for i in range(n):
    for j in range(n):
        print(A[i][j],end=' ')
    print()
if(A[0][0]+A[0][1]+A[0][2]==A[1][0]+A[1][1]+A[1][2]==A[2][0]+A[2][1]+A[2][2]):
    print('magical')
else:
    print('not magical')




