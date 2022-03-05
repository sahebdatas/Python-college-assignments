print("printing series....")
n=int(input("Enter no of rows for each series:"))
for i in range(n):
 print(' '*(n-i), end='')
 print(' '.join(map(str, str(11**i))))