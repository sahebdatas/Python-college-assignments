print("***Multiple series of pyramid printing***")
n=int(input("Enter no of rows for each series:"))
print("printing series 1:-")
a=0
for i in range (0,n):
    for j in range(0,i+1):
        i=i+1
        a=a+1
        print(a,end=" ")
    print()
print("printing series 2:-")
for i in range (0,n):
    for j in range(0,i+1):
        i=i+1
        a=a+1
        print("1",end=" ")
    print()
print("printing series 3:-")
a=0
for i in range (0,n):
    a=a+1
    for j in range(0,i+1):
        i=i+1
        print(a,end=" ")
    print()