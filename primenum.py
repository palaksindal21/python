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