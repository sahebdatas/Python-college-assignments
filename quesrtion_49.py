print("***given set is superset of itself and superset of another given set***")
print("creating sets...")
s1=set([10,20,30,40,50])
s2=set([60,70,80,90])
print("set 1=",s1)
print("set 2=",s2)
print("checking if set 1 is superset of itself:",s1.issuperset(s1))
print("checking if set 1 is superset of set 2",s1.issuperset(s2))