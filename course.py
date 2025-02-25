maths = int(input("Enter marks in Mathematics: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))

total = maths + physics + chemistry

if maths >= 65 and physics >= 55 and chemistry >= 50 and total >= 190:
    print("You are eligible for admission.")
else:
    print("you are not eligible for admission.")