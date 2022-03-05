print("***Printing the HCF between two numbers***")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num2>num1:
    mn=num1
else:
    mn=num2
for i in range(1,mn+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print("HCF=",hcf)