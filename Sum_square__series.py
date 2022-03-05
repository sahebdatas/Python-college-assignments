print("***Printing Series: S= 1^2 +2^2+. . . . + n^2***")
n=int(input("Enter the nth no:"))
sum=0
for i in range(1,n+1):
    sum=sum+i**2
    print(i,"^ 2 ",end="")
    if i!=n:
        print("+ ",end="")
print("=",sum)