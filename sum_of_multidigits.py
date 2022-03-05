print('''****print sum of  the digits of  a multidigit integer.****''')
i=(int(input("Enter a multi-digit integer:-\n")))
if(i<10):
    print("it is a single digit number")
    exit()
i1=i
sum=0
while(i>0):
    j=i%10
    i=i//10
    sum=sum+j
print("Sum of",i1,"=",sum)