print("****program to remove duplicates from a list****\n")
l1=[2,3,4,5,5,4,8,3,9]
print("creating new list...\n")
new_l1 = []
print("filltering dublicate values...\n")
for i in l1:
    if i not in new_l1:
        new_l1.append(i)
print ("The original list is : " +  str(l1))
print ("The Filtered list is : " +  str(new_l1))