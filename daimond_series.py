print("printing series....")
n=int(input("Enter no of rows for each series:"))
m=n
for i in range(1,n+1):
    for j in range(1,m):
        print(end=" ")
    for k in range(1,2*i):
        print("*",end="")
    m-=1
    print()
l=2
for i in range(n-1,0,-1):
    for j in range(1,l):
        print(end=" ")
    for k in range(2*i-1,0,-1):
        print("*",end="")
    l+=1
    print()