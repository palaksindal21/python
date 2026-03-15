#employee salary calculator
class Employee:
    def __init__(self):
        self.name = input("Enter name:")
        self.designation = input("Enter designation:")
        self.monthly_salary = int(input("Enter your monthly salary:"))
    def annual_salary(self):
        self.annual_salary = self.monthly_salary*12
        print("annual salary of",self.name,"is",self.annual_salary)
obj1 = Employee()
obj1.annual_salary()