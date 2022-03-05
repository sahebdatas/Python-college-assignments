print("printing series....")
n=int(input("Enter no of rows for each series:"))
x=0
for i in range (0,n):
    for j in range(0,x+1):
        i=i+1
        print("*",end="")
    x=x+2
    print()