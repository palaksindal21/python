# A method get_details() that prints the student’s details.
class Student :
    def __init__(self) :
        self.name = input("Enter the name of the student : ")
        self.rollno = int(input("Enter the roll number of the student : "))
        self.grade = input("Enter the grade of the student : ")
        self.age = int(input("Enter the age of the student : "))

    def display(self) :
        print("Name of the student is : ", self.name)
        print("Roll number of the student is : ", self.rollno)
        print("Grade of the student is : ", self.grade)
        print("Age of the student is : ", self.age)

obj1 = Student()
obj1.display()
obj2 = Student()
obj2.display()
