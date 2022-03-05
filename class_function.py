class student:
    def __init__(self, student_name, student_id):
        self.name=student_name
        self.id=student_id
    def display(self):
        print("my name is:",self.name)
        print("my id is:",self.id)
    # def myfunc(student_class):
    #     print("Displaying")
    #     print("class=",student_class)
    # print("name",self.name)
    # print("id",self.id)
s1=student("Saheb",22)
s1.display