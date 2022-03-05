print("***Printing Series: 1+1/2+1/3+1/4+........+1/n***")
n=int(input("Enter the nth no:"))
sum=0
for i in range(1,n+1):
    sum=sum/i+1
    print(i,"+",1,end="")
    if i!=n:
        print("/",end="")
print("=",sum)