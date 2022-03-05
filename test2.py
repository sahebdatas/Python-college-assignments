class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print("Hello my Name is ",self.name)
        print("And my ID is", self.id)

p1 =student ("saheb", 22)
p1.display()