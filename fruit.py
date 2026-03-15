# create a list of fruit and print the name of  each fruit using loop.
list = ["apple","banana","mango","grapes","orange","cherry","pineapple","papaya","watermelon"]
for i in list:
    print(i)

# Reverse a string entered by the user.
string = input("Enter a string: ")
print(string[::-1])

# Find the largest number in a list.
li = []
n = int(input("enter the number of elements you want to enter"))

for i in range(n):
        num = int(input("Enter the element of list"))
        li.append(num)
        if i > num :  
            print("the highest number:",i)
        