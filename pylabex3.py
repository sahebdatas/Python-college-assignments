print("***Manupulating Tuple***")
t1 = (1,2,3,5,6,7,8,9,10,11);
l1 = list(t1)
print(type(l1))
res = [i for i in l1 if not (i % 2 != 0)]
print ("List after removal of odd values : " + str(res))
t1 = tuple(l1)
print(type(t1))