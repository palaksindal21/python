#for every iteration of outer loop inner loop get completely executed.
for i in range(5):
    for j in range(3):
        print(i,j)
        
        
for i in range(10,51):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()

#Pallindrome number using loop
n = int(input("enter number:"))
s = str(n)
print(s,type(s))
if s == s[::-1]:
    print("pallindrome")
else:
    ("not a pallindrome")

for i in range(6):
    print("*"*5)

for i in range(1,6):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)

k = 4
for i in range(0,5):
    print(" "*k+"*"*(2*i+1))
    k = k-1















#Pallindrome number in given range
# for i in range(100,2000):
#     s = str(i)
#     if s == s[::-1]:
#         print(i,end=" ")