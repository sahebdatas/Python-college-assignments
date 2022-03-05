print("***Binary To Integer***")
num=int(input("Enter a binary Number:"))
cpnum=num
sum=0
i=0
while num>0:
    rem=num%10
    sum=sum+rem*pow(2,i)
    num=num//10
    i=i+1
print("converting", cpnum, "to integer...")
print(sum)