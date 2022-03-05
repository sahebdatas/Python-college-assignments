print("****Print largest and smallest number in the list****\n")
n = int(input("Enter number of elements : "))
lst=[]
print("Enter the items in the list:")
for i in range(0, n):
    a = int(input())
  
    lst.append(a)
print("Printing the list:",lst)
print("largest number in the list is",max(lst))
print("smallest number in the list is",min(lst))