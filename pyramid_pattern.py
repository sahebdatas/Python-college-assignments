print("***printing pyramid series 0,1***")
a=0
b=1
n = int(input("Enter the number of rows:"))
for i in range(0, n):
        for j in range(0, i + 1):
                print(a, end=" ")
                if a==0:
                    a=1
                else:
                    a=0
        print()
        b=b+1
        if(b%2==0):
            a=1
        else:
            a=0
