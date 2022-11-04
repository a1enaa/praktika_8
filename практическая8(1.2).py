m=4
n=3
A=[]
for i in range(m):
    B=[]
    for i in range(m):
        B.append(int(input()))
    A.append(B)
for i in range (m):
    for j in range(n):
        print(A[i][j],end=' ')
    print()
for i in range(m):
    max=A[0][j]
    for j in range(n):
        if A[i][j]>max:
            max=A[i][j]
    print('максимальный элемент:',max)
print()
for i in range(m):
    min=A[i][j]
    for j in range(n):
        if A[i][j]<min:
            min=A[i][j]
    print('минимальный элемент:',min)
print()










