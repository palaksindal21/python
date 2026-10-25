#wap to determine the sum of n natural number.
'''
n = int(input("enter range:"))
sum = 0

for i in range(1,n+1):
    sum = sum + i
print("sum:",sum)

#wap to determine the sum of n number.
n = int(input("enter range:"))
sum = 0

for i in range(n):
    num = int(input("enter number:"))
    sum = sum + num

print(sum)
'''
#wap to determine the sum of  even number among n number.
n = int(input("enter range:")) #7
sume = 0
sumo = 0
for i in range(n):
    num = int(input("enter number:"))
    if num%2==0 :
       sume=sume+num
    else :
        sumo=sumo+num


#Pallindrome number
num1 = int(input("Enter number:"))
temp = num1
sum = 0
while num1 > 0:
   last = num1 % 10 #121
   sum = (sum * 10) + last
   num1=num1 // 10
if temp == sum:
   print(temp,"is a pallindrome number")
else:
   print(temp,"is not a pallindrome number")


#Maximum number
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1>num2 :
    print(num1,"is maximum number")
else :
    print(num2,"is maximum number")

#Area of rectangle and square
Length = int(input("enter length of rectangle:")) 
Breadth = int(input(" Enter breadth of rectangle:")) 
side = int(input(" Enter side of square "))

area_of_rectangle = Length*Breadth
area_of_square = side*side

if area_of_rectangle>area_of_square :
    print(area_of_rectangle," Area of rectangle is greater") 
else : 
    print(area_of_square," Area of square is greater") 


#Smallest number
num1 = int(input("Enter first number:")) 
num2 = int(input("Enter second number:")) 
num3 = int(input("EEnter third number:")) 

if num1<num2 and num1<num3 :
    print(num1,"is smallest ") 
elif num2<num1 and num2<num3 :
    print(num2,"is smallest ") 
else:
    print(num3," is smallest")

#Checking square
Length = int(input("enter length of rectangle:")) 
Breadth = int(input(" Enter breadth of rectangle:")) 

if Length==Breadth :
    print(" It is a square") 
else :
   print(" It is not a square")


#Marriage age checking

age = int(input("Enter your age:"))
gender = input("enter your gender(Male/Female):")

if age>=18 and gender=="Female":
    print("You are eligible for marriage")

elif age>=21 and gender=="Male":
    print("You are eligible for marriage")
else:
    print("You are not eligible for marriage")


#maximum between 3 numbers
num1 = int(input("Enter first number:")) 
num2 = int(input("Enter second number:")) 
num3 = int(input("EEnter third number:")) 

if num1>num2 and num1>num3 :
    print(num1,"is maximum ") 
elif num2>num1 and num2>num3 :
    print(num2,"is maximum ") 
else:
    print(num3," is maximum")

#grade check
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


#cost of pen
number_of_pen = int(input("Total number of pen:")) 
cost_of_1pen = int(input("Cost of one pen:")) 
cost_of_pens = number_of_pen*cost_of_1pen

if  cost_of_pens>1000 :
     discount = cost_of_pens*20/100
     print("you have to pay",cost_of_pens-discount,"rs") 
else :
     discount = cost_of_pens*10/100
     print("you have to pay",cost_of_pens-discount,"rs")


#Attendance
class_held = int(input("Enter total classes held: "))
class_attended = int(input("Enter total classes atended: "))

percentage = class_attended/class_held * 100

if percentage>=75 and percentage<=100 :
    print("You are allowed to sit in exam")
else : 
    print("You are not allowed to sit in exam")


#armstrong number
num1 = input("Enter number:")
n = len(num1)
num = int(num1)
temp = num
sum = 0
while num > 0 :
    last = num % 10
    sum = sum + (last**n)
    num = num // 10
if sum == temp:
    print("Armstrong number")
else :
    print("Not a Armstrong number")

#Eligible for admission
maths = int(input("Enter marks in Mathematics: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))

total = maths + physics + chemistry

if maths >= 65 and physics >= 55 and chemistry >= 50 and total >= 190:
    print("You are eligible for admission.")
else:
    print("you are not eligible for admission.")


# 2.Palindrome Checker
# Write a program that checks if a given word is a palindrome.
num = int(input("Enter number:")) #taking input from user
temp = num
sum = 0

while num>0:
    num1 = num % 10
    sum = (sum*10) + num1
    num = num//10
if temp == sum:
    print("Given number is a pallindrom.")
else:
    print("Given number is not a pallindrome.")


#Attendance check
class_held = int(input("Enter total classes held: "))
class_attended = int(input("Enter total classes atended: "))

percentage = class_attended/class_held * 100

if percentage>=75 and percentage<=100 :
    print("You are allowed to sit in exam")
else : 

    print("You are not allowed to sit in exam")


#Create a list of numbers, then write a program that prints the square of each number in the list.
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
for i in list:
    square = i**2
    print("Square of",i,"is",square,".")


#bank account and display details
class BankAccount:
    def __init__(self):
        self.account_holder = input("Enter your name: ")
        self.balance = int(input("Enter your balance: "))
    def withdraw(self):
        self.amount = int(input("enter amount you want to withdraw:"))
        if self.amount > self.balance:
            print("insufficient balance")
        elif self.amount < 100:
            print("account balance is low")
        else:
            self.balance = self.balance - self.amount
            print("your balance is:",self.balance)
    def deposit(self):
        self.deposit = int(input("enter amount you want to deposit:"))
        self.balance = self.balance +self.deposit
        print("your balance is:",self.balance)
    def display_balance(self):
        print("your balance is:",self.balance)
obj1 = BankAccount()
obj1.withdraw()
obj1.deposit()
obj1.display_balance()


#Factor of number
num = int(input("Enter a number:"))
print("Factors of",num,"are:")
for i in range(1,num+1):
    if num%i == 0:
        print(i)


#check factorial
num = int(input("Enter a number: "))
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial is", fact)

for num in range(1,num+1):
    fact = fact*num

print("factorial:",fact)

#Fibonacci series
n = int(input("enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#voting eligibility
class VotingEligibility :
    def __init__(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
    def candidate(self):
        if self.age < 18 :
            print("you are not eligible")
        else :
            print("you are eligible")
obj1 = VotingEligibility()
obj1.candidate()


# Swapping of variables without using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a,b = b,a
print("Value of a is",a)
print("Value of b is",b)


# Swapping of variables by using third variable
temp = b
b = a
a = temp

print("Value of a is", a)
print("Value of b is", b)


#armstrong number
num1 = input("Enter number:")

n = len(num1)
num = int(num1)
temp = num
sum = 0
while num > 0 :
    last = num % 10
    sum = sum + (last**n)
    num = num // 10
if sum == temp:
    print("Armstrong number")
else :
    print("Not a Armstrong number")

#prime number
num = int(input("Enter number:"))

if num>1:
   for i in range(2,num):
      if num%i == 0:
         print(num,"is not a prime number")
         break
   else:
         print(num,"is prime number")

else:
   print(num,"is not a prime number")

# ASCII value of a character

char = 'a'
print(ord(char))   # ord is built in function for printing ascii value