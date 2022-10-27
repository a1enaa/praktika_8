n=int(input())
A=[]
sum=0
c=0
for i in range(n):
    B=[]
    for j in range(n):
        B.append(int(input()))
    A.append(B)
for i in range(n):
    for j in range(n):
        print(A[i][j],end=' ')
    print()
for i in range(n):
    for j in range(n):
         if j>i:
            sum=sum+A[i][j]
            if A[i][j]>0:
                c=c+1
print(sum)
print(c)
