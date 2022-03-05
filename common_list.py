print("***Return TRUE if anything common in between 2 list***")
def list_insertion():
    a=int(input("enter the max array element:"))
    arr=[]
    for i in range (a):
        b=int(input("enter the array element:"))
        arr.append(b)
    return(arr)
print("inserting list 1 values...")
lst1=list_insertion()
print("inserting list 2 values...")
lst2=list_insertion()
com=False
print("Finding common values...")
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j]:
            com=True
print("list 1=",lst1)
print("lsit 2=",lst2)
print("presence of common value:",com)