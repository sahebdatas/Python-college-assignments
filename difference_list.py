print("***Difference between 2 list***")
def list_insertion():
    a=int(input("enter the max array element:"))
    arr=[]
    for i in range(a):
        b=int(input("enter the array element:"))
        arr.append(b)
    return(arr)
print("inserting list 1 values...")
lst1=list_insertion()
print("inserting list 2 values...")
lst2=list_insertion()
print("differeciating between 2 lists....")
print(lst1,"-",lst2,"=",list(set(lst1)-set(lst2))+list(set(lst2)-set(lst1)))