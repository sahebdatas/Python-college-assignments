print('''****print the series:-1   3   7   13   21   31 ****''')
l=(int(input("Enter the series limit:-\n")))
i=0
ans=0
while(ans<l):
    ans=i*i+i+1
    print(ans, end=" ")
    i=i+1
print("\n***series has ended***")