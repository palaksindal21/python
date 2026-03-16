
#wap to determine the sum of n natural number.

n = int(input("enter range:"))
sum = 0

for i in range(1,n+1):
    sum = sum + i
print("sum:",sum)

# #wap to determine the sum of n number.
n = int(input("enter range:"))
sum = 0

for i in range(n):
    num = int(input("enter number:"))
    sum = sum + num

print(sum)

# #wap to determine the sum of  even number among n number.
n = int(input("enter range:")) #7
sume = 0
sumo = 0
for i in range(n):
    num = int(input("enter number:"))
    if num%2==0 :
       sume=sume+num
    else :
        sumo=sumo+num

#wap to find sum of digits of a number
num1 = int(input("Enter a number:"))
sum = 0

while num1>0:
    digit = num1%10
    sum = sum + digit
    num1 = num1//10

print(sum)

# Count number of digits in a number
num2 = input("Enter a number:")
digits = len(num2)
print(digits)


count = 0
while num2>0:
    num2 = num2//10
    count += 1

print("number of digits:",count)