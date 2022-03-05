print('''***Write a python program to count the number of strings where the
string length is 2 or more and the first and last character are same from a
given list of strings
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2''')
lst=["saheb",1221,3333,"sayan","ss"]
count=0
for i in range (0,len(lst)):
    a=str(lst[i])
    if(len(a)>2):
        l=len(a)-1
        if(a[0]==a[l]):
            count=count+1
print("Printing Solution...")
print("printing the list:",lst)
print("count=",count)