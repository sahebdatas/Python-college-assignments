print("****printing all armstrong number between 1-500****")
print("printing armstrong no...")
for num in range(1,501):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=int(temp//10)
      if sum==num:
           print (num)