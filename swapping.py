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