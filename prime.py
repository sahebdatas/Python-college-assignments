lower = 1
upper = 9999
t=1
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if t<=20:
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
           t=t+1