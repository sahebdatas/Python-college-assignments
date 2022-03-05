print("***program to get the frequency of the elements in a list file.***")
lst = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B','E',2,1,2,4,7,2,1,7]
f = {}
for i in lst:
   if i in f:
      f[i] += 1
   else:
      f[i] = 1
print(f)