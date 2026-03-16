# pallindrom number checker
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

# reversing a number
  
num = int(input("Enter a number: "))
reverse = 0

while num>0:
   last_digit = num % 10
   reverse = reverse*10 + last_digit
   num = num//10

print("Reverse:",reverse)
