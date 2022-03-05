print("****Printing fibonaci series****")
t=(int(input(("Enter no of terms:\n"))))
n1,n2=0,1
count=0
print("printing the series...")
while count < t:
     print(n1)
     s = n1 + n2
     n1 = n2
     n2 = s
     count += 1
print("***Series had ended***")
