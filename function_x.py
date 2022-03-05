# Write a program to find the value of the function :

#        F(x)=3x2+5      if     x<= 10

#               =5x            if     x>10   and x<=20

#               =2x2-x+9   if     x>20

#        Input value of x
print("*****Input x to get its function****\n")
x=(int(input("Enter X\n")))
if(x<=10):
    x=3*2+5
    print("F(x)=3x2+5 =>",x)
elif(x>10 and x<=20):
    x=5*x
    print("F(x)=5x =>",x)
elif(x>20):
    x==((2*2)-x)+9
    print("F(x)=2x2-x+9 =>",x)