age = int(input("Enter your age:"))
gender = input("enter your gender(Male/Female):")

if age>=18 and gender=="Female":
    print("You are eligible for marriage")

elif age>=21 and gender=="Male":
    print("You are eligible for marriage")
else:
    print("You are not eligible for marriage")