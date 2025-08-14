class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 0
        self.salary = 50000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"employee is travelling to {destination}")

# creating instance of class 
sam = employee()

# print(sam.id,sam.designation,sam.salary)
sam.travel("delhi")
print(sam.travel)
