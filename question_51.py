print("***given set has no elements in common with other given set***")
print("creating sets...")
s1 = {10,20,30}
s2 = {40,50,60}
s3 = {30,40,50}
print("set1=",s1)
print("set2=",s2)
print("set3=",s3)
print("Checking set1 has no elements in common with set2:")
print(s1.isdisjoint(s2))
print("Checking set1 has no elements in common with set3:")
print(s1.isdisjoint(s3))