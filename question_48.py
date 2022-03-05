print("***program to check if two given sets have no elements in common***")
x = {1,2,3,4,5}
y = {5,6,7,8,9}
z = {10}
print(type(x))

print("If two given sets have no elements in common")
print("Compare x and y:")
print(x.isdisjoint(y))
print("Compare x and z:")
print(z.isdisjoint(x))
print("Compare y and z:")
print(y.isdisjoint(z))
