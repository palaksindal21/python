num = int(input("Enter a number: "))
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial is", fact)



for num in range(1,num+1):
    fact = fact*num

print("factorial:",fact)