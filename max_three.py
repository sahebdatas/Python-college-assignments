print("*****Input 3 integers to find the max among the 3****\n")
a=(int(input("Enter first no\n")))
b=(int(input("Enter second no\n")))
c=(int(input("Enter last no\n")))
if (a >= b) and (a >= c): 
        print("maximum of 3 integer is ",a)
  
elif (b >= a) and (b >= c): 
        print("maximum of 3 integer is ",b)
else: 
        print("maximum of 3 integer is ",c)