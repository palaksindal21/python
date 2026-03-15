'''
for i in range(10,100,10):
    print(i,end=" ")


for j in range(100,10,-10):
    print(j,end=" ")
          
for k in range(-20,-60,-5):   #for negative numbers
    print(k,end=" ")
'''

# WAP to create a multiplication table for any table
'''
num = int(input("enter number:"))
num2 = num+1
num3 = num-1
for i in range(1,11):
    print(num,"x",i,"=",num*i,end="\t")
    print(num2,"x",i,"=",num2*i,end="\t")
    print(num3,"x",i,"=",num3*i)
   # print(num+1,"x",i,"=",(num+1)*i)
'''
#n=7
# 1 2 4 8 16 32 64 

#n=9
# 1 2 4 8 16 32 64 128 256
'''
n = int(input("Enter number:"))

for n in range(n):
    print(2**n,end=" ")

'''

#WAP 40 45 50 55 ....................140
for i in range(40,141,5):
    print(i,end=" ")

for i in range(40,126,5):
    if i%6!=0:
       print(i,end=" ")
    
#WAp to iterate the first 10 numbers and in each iteration print the sum of teh current and previous number
sum = 0
for i in range(11):
    print("current number",i)
    sum = i + (i-1)
    print("sum",sum)