#Print hello world
print("Hello World!!")

#Add two numbers
num1 = int(input("Enter first number"))
num2 =int(input("Enter second number"))
sum = num1 + num2
print("sum:",sum)

#swap two numbers
a = int(input("Enter first number"))
b=int(input("Enter second number"))
a,b = b,a
print("a:",a)
print("b:",b)

#Find the largest of two numbers
num1 = int(input("Enter first number"))
num2 =int(input("Enter second number"))

if num1 > num2:
    print(num1," is largest number")
else:
    print(num2," is largest number")

#Find the largest of three numbers
num1 = int(input("Enter first number"))
num2 =int(input("Enter second number"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    print(num1," is largest number")
elif num2 > num1 and num2 > num3:
    print(num2," is largest number")
else:
    print(num3," is largest number")

#Check even or odd number
num = int(input("Enter a number:"))

if num%2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

#Check wether a number is positive negative or zero
num = int(input("Enter a number:"))

if num < 0:
    print(num," is negative number")
elif num > 0:
    print(num," is a positive number")
else:
    print("It is a zero")
          
#Find the factorial of number
num = int(input("Enter a number:"))
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial of ",num, "is: ", fact)

#Generate fibonacci series
terms = int(input("Enter number of terms: "))
a = 0
b = 1
c = a + b

while terms >= 0:
    print(a, end=" ")
    a = b
    b = c

for i in range(terms):
    print(a, end=" ")
    a = b
    b = c

#Check wether a number is prime
n = int(input("Enter a number:"))

if n > 1:
    for i in range(2, n+1):
        if n % i== 0:
            print(n,"is not a prime number")
        else:
            print(n," is a prime number")
else:
    print(n,"is not a prime number")

#Print all prime numbers in a range
n1 = int(input("Enter starting of range:"))
n2 = int(input("Enter ending of range: "))

for num in range(n1, n2+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end="")

#Find the sum of n natural numbers
end = int(input("Enter range: "))
sum = 0
for i in range(1,end+1):
    sum = sum + i
print("Sum of n natural number is: ",sum)


#Find the sum of digits of a number
num = int(input("Enter a number:"))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits: ", sum)


#Count the digits in a number
num = int(input("Enter a number:"))
count = 0

while num > 0:
    digit = num % 1
    count = count + 1
    num = num // 10

print("Total digits in ",num,"are: ",count)

#Reverse a number
num = int(input("Enter a number:"))
reverse = 0

while num > 0:
    last = num % 10
    reverse = (reverse * 10) + last
    num = num // 10

print("Reverse: ", reverse)

#Check whether a number is pallindrome
num = int(input("Enter a number:"))
temp = num
sum = 0

while num > 0:
    last = num % 10
    sum = (sum * 10) + last
    num = num // 0

if temp == sum:
    print("It is a pallindrome number")
else:
    print("It is not a pallindrome number")

#check whether a number is armstrong number
num = int(input("Enter a number:"))
temp = num
length = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = (digit**length) + sum
    num = num // 10

if temp == sum:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number")

#Find the greatest common factor GCD/HCF
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1

for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD: ", gcd)

#Find the Least common multiple
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = max(a,b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm = lcm + 1
print("LCM:", lcm)

#Print the multiplication table of a number
num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num * i)

#Print all factors of a number
num = int(input("Enter a number:"))
print("Factors of ",num,"are: ")
for i in range(1, num+1):
    if i % 2 == 0:
        print(i)

#Check whether a number is perfect number
num = int(input("Enter a number:"))
total = 0
temp = num 

for i in range(1,num-1):
    if num % i == 0:
        total = total + i
if total == temp:
    print("It is a perfect number")

#Check wether a number is strong number
num = int(input("Enter a number:"))
total = 0
temp = num 

while num > 0:
    digit = num % 10
    fact = 1
    for i in range(1,digit+1):
        fact = fact * i
    total = total + fact
    num = num//10

if temp == total:
    print("It is strong number")
else:
    print("It is not a strong number")

#check wether a number is automorphic number
num = int(input("Enter a number:"))         
square = num ** 2
if str(square).endswith(str(num)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

#Convert Celsius into fahrenheit
c = int(input("Enter temperature in Celsius: "))
f =(9/5 * c) + 32
print("Temperature in Fahrenheit: ",f)

#Convert fahrenheit into celsius
f = int(input("Enter temperature in Fahrenheit: "))
c = 5/9 * (f - 32)
print("Temperature in Celsius:", c)

#Find the area of circle
radius = int(input("Enter radius of circle: "))
area = 3.14 * radius * radius
print("Area of cirle: ", area)

#Calculate simple interest
p = float(input("Enter principle amount:"))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

si = (p*r*t)/100
print("simple interest: ", si)

#Calculate compound interest
p = float(input("Enter principle amount:"))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

amount = p*(1 + r/100)**t 
ci = amount - p
print("Compound interest: ",ci)

#Find the square root of number
num = int(input("Enter a number:"))
root = num**0.5
print("Squareroot: ", root)

#Find the cube of number
num = int(input("Enter a number:"))
cube = num ** 3
print("Cube of ", num, "is ", cube)

#Find the power of number
num = int(input("Enter a number:"))
power = int(input("Enter power: "))

print("Power of number: ", num**power)

#Generate random numbers
import random

num = random.randint(1, 100)
print(num)