class_held = int(input("Enter total classes held: "))
class_attended = int(input("Enter total classes atended: "))

percentage = class_attended/class_held * 100

if percentage>=75 and percentage<=100 :
    print("You are allowed to sit in exam")
else : 
    print("You are not allowed to sit in exam")