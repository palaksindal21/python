'''
Function - reusable block of code.
- A function is a block of code which only runs when it is called.
- You can pass data, known as parameters, into a function.
- Functions save time and increase the quality of your code.
- You can reuse a function if you need to perform the same task multiple times.
- user defined & predefined functions
- features-- > 1) reusability 2) modularity - broken down complex problems into n smaller problems 3) readability - easy to understand 4) maintainability - easy to modify 
- types of functions - 1) built-in functions 2) user defined functions 
- types of user defined functions - 1) normal functions 2) lambda functions 3) nested
- block c, c++, java - {} ,python - indentation
- defined by - def keyword
- with return---> having parameter , not having parameter
- without return ---> having parameter , not having parameter
'''

def fun() :
    print("Hello, World!")  #without return , not having parameter

fun()

def func() :
    print("Hello, World!")  #without return , not having parameter

a = func()
print(a)#none

def function() :
    return("Hello, World!")  #with return , not having parameter

a = function()
print(a) #my function

def math(a,b) :
    add = a + b
    substract = a - b
    multiplication = a * b
    division = a / b
    print("sum:",add)
    print("difference:",substract)
    print("multiplication:",multiplication)
    print("division:",division)
a = int(input("enter number 1:"))
b = int(input("enter number2:"))

math(a,b) #parameter passing   
# add(2,4) argument passing


#Function calling inside the body of function
#wap to create a small console based project having following functionalities(Employee management system)
#insert record
#display record
# search name 
# search gender
# update record
# filter experience
# delete last record
# delete any record
