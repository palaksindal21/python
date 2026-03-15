num = int(input("Enter number:"))

sqr = num**2

if num < 1:
    print(num,"is not a prime number.")
elif num > 1:
    for i in range(num,sqr):
        num % i == 0
    print(num,"is not a prime number.")
else:
    print(num,"is a prime number.")