<<<<<<< HEAD
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
=======
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
>>>>>>> b4a6aa7 (added programs)
    print("Not a Armstrong number")