
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