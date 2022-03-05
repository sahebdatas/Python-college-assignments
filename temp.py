student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
a="id1"
print("printing the dictionary")
print(student_data)
a=(len(student_data))
for i in range (1,a+1):
    d="id"+str(i)
    print("d=",d)
    for j in range (1,i):
        e="id"+str(j+1)
        print("e=",e)
        if(student_data[d]==student_data[e]):
            student_data.pop()

print("printing the new dictionary.....")
print(student_data)