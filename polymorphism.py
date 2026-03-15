'''
polymorphism - whenever an object behave differently in different contexts or situations then the concept is known as polymorphism.
polymorphism is of two types
Compile time polymorphism
1. function overloading #python doesn't support function overloading
2.operator overloading

Run time polymorphism
3. function overriding

'''

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    
    def display(self):
        print(self.real,"+",self.imaginary,"i")
    def __add__(self):
       pass
    