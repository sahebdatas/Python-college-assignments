print("***python program to find the second smallest and second largest number in a list***")
a=int(input("enter the max array element:"))
arr=[]
for i in range(a):
    b=int(input("enter the array element:"))
    arr.append(b)
print(arr)
print("finding the required number...")
arr.sort()
ll=len(arr)
print("The smallest Number is:",arr[0])
print("The second smallest Number is:",arr[1])
print("The second largest Number is:",arr[ll-2])
print("The largest Number is:",arr[ll-1])