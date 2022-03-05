print("****Print factorial of number****\n")
num=(int(input("enter a number to get its factorial\n")))
num1=num
factorial=1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   while(num>0):
       factorial=factorial*num
       num=num-1
   print("The factorial of",num1,"is",factorial)