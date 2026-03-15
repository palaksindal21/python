#create a class with age category
class Age :
    def __init__(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
    def age_category(self):
        if self.age < 12:
            print(self.name,"is child")
        elif self.age <= 12 and self.age >= 18:
            print(self.name,"is teenager")
        else:
            print(self.name,"is adult")
obj1 = Age()
obj1.age_category()
obj2 = Age()
obj2.age_category()