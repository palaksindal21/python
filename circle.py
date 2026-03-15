#circumference and area of circle
class Circle :
    def __init__(self):
        self.radius = float(input("enter radius of circle:"))
    def area(self):
        self.area = self.radius*self.radius
        print("area of circle is :",self.area)
    def circumference(self):
        self.circumference = 2*3.14*self.radius
        print("circumference of circle is :",self.circumference)
obj1 = Circle()
obj1.area()
obj1.circumference()