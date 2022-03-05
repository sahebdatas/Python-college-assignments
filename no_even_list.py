print("***printing the list without even no's***")
a=int(input("enter the max array element:"))
arr=[]
ls=[]
c=0
for i in range(a):
    b=int(input("enter the array element:"))
    arr.append(b)
print(arr)
print("detecting the even from the list...")
for i in range (a):
    if arr[i]%2==0:
        ls.append(i)
print("removing the even from the list...")
for i in range (len(ls)):
    
    arr.pop(ls[i]-c)
    c=c+1
print("printing the new list..")
print(arr)