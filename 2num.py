#Wap to return their product only if the product is lower than or equal to 1000.otherwise print sum.

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

sum = num1 + num2
product = num1*num2

if product <= 1000 :
    print("the result is",product)
else :
    print("the result is",sum)

