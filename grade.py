marks = int(input("enter your marks:"))
if marks >= 80:
    print("A grade")
elif marks >= 60 and marks < 80:
    print("B grade")
elif marks >= 50 and marks < 60:
    print("C grade")
elif marks >= 45 and marks < 50:
    print("D grade")
elif marks >= 25 and marks < 45:
    print("E grade")
else:
    print("F grade")