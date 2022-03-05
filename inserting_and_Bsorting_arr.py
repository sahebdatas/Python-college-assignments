a=int(input("enter the max array element:"))
arr=[]
for i in range(a):
    b=int(input("enter the array element:"))
    arr.append(b)
print(arr)
print("Printing in sorted manner")
for i in range (len(arr)):
    for j in range (len(arr)-i-1):
        if arr[j]>arr[j+1]:
            x=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=x
print(arr)