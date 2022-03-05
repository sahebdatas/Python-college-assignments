print("****Multiplies all the items in a list****\n")
n = int(input("Enter number of elements : "))
l1=[]
print("Enter the items in the list:")
for i in range(0, n):
    a = int(input())
  
    l1.append(a)
print("Printing the list:",l1)
sum=l1[1]
for i in range (1,len(l1)):
    a=l1[i]
    sum=sum*a
print("Multiply list:",sum)