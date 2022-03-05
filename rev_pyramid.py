print("***Reverse pyramid printing***")
n=int(input("Enter no of rows:"))
for i in range (n,0,-1):
    for j in range(0,i):
        i=i+1
        print("*",end="")
    print()