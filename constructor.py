#parameterized constructor
class Highest:
    def __init__(self,num1,num2,num3): #self holds the reference of object  #parameterized
        self.n1 = num1
        self.n2 = num2
        self.n3 = num3
    def high(self):
        if self.n1>self.n2 and self.n1>self.n3:
            print(self.n1,"is highest")
        elif self.n2>self.n1 and self.n2>self.n3 :
            print(self.n2,"is highest")
        else:
            print(self.n3,"is highest")
obj1 = Highest(24,5,6)
obj1.high()


#class variable in python --- in cpp just like our static variable whose value remain same for all the instances of a class,in python we have class variable, all instances used list value and may override this value .
# Note - in cpp we want to manipulate (override) the value holds by static variable then we should use class to do so and changes get reflected in all instances of a class.But in python override data is only associated with instance,who changed it.

class High:
    data = 90 #class variable 
    def __init__(self,a,b):
        self.d1=a
        self.d2=b