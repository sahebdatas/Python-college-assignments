a=int(input("enter the max array element:"))
arr=[]
for i in range(a):
    b=int(input("enter the array element:"))
    arr.append(b)
print(arr)
# print("Printing in selection manner")

# for i in range (a):
#     small=null
#     loc=null
#     for j in range (i,a):
#         if arr[i]>arr[j]:
#             small=arr[j]
#             loc=j
#     arr[loc]=arr[i]
#     arr[i]=small
# print(arr)
for i in range(a):
    small = i
    for j in range(i+1, a):
        if arr[small] > arr[j]:
            small = j
    arr[i], arr[small] = arr[small], arr[i]
print(arr)
