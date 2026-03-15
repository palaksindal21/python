#display area and perimeter of rectangle
class Rectangle:
    def __init__(self):
        self.length=int(input("enter the length:"))
        self.breadth=int(input("enter the breadth:"))
    def area(self):
        self.area = self.length*self.breadth
        print("area of rectangle is:",self.area)
    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        print("perimeter of rectangle is:",self.perimeter)
obj1=Rectangle()
obj1.area()
obj1.perimeter()
