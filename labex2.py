print("***Instance Counter***")
class saheb:
    counter = 0
    def __init__(self):
        saheb.counter += 1

a = saheb()
b = saheb()
c = saheb()
print(saheb.counter)