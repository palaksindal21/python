'''
lis = [2,3,4,5]
print(lis)
lis.append("66")   #append function
print(lis)

#extend function
lis = [2,3,4,5,6,7,8]
print(lis)
lis2 = [9,10,11,12,13]
lis.extend(lis2)
lis2.extend(lis)
print(lis)


#index function
lis = [2, 3, 4, 5, 6, 7, 8, 9,4, 10, 11, 12, 13,4]
print(lis)
index_number = lis.index(4)
index_number = lis.index(4,3)
print(index_number)
index_number = lis.index(4,9)
print(index_number)

#count() --> frequency of element
lis = [2, 3, 4, 5, 6, 7, 8, 9,4, 10, 11, 12, 13,4]
n = lis.count(4)
print(n)

#insert function
lis = [2, 3, 4, 5, 6, 7,8, 9,4, 10, 11, 12, 13,4]
lis.insert(4,10)
print(lis)

#len(),max(), min(), sum()
lis = [2, 3, 4, 5, 6, 7,8, 9,4, 10, 11, 12, 13,4]
names = ["Ajay","Suyash" ,"Rahul","Raj","Rahul","Reeta"]
print("length",len(lis))
print("max",max(lis))
print("min",min(lis))
print("sum",sum(lis))
print("max",max(names))


#wap to create a list with n elements also find the maximumm ,the minimum, sum of all elements....
n = int(input("enter range:"))
sum = 0
list3 = [] #list() function for creating a list
for i in range(n):
    num = int(input("enter a number:"))
    list3.append(num)
    sum = sum + num

print(list3)
print("maximum element",max(list3))
print("minimum element",min(list3))
# ("sum:",sum(list3(print))
print("sum:",sum)


n = int(input("enter range:"))
num = int(input("enter number:"))
li = [num]
max = num

for i in range(n-1):
    num = int(input("enter number:"))
    li.append(num)
    li.insert(0,num)
    if num > max :
        max = num
    
print(li)
print("maximum",max)
'''


list = ["ajay","anoop","akash","ritu","anoop","Komal","anoop"] #you have to remove anoop from the given list.
list4 =["ajay","anoop","akash","ritu","anoop","Komal","anoop"]
while "anoop" in list4 :
     list4.remove("anoop")
print(list4)

#WAP to create a list of n students example - [["ajay",24,"science"],["aman",33,"art"]["vikas",31,"commerce"]]
n = int(input("How many records do you want to insert:"))
stu_record = []
names = []
ages = []
streams = []
for i in range(n):
     name = input("Enter name:")
     age = int(input("Enter age:"))
     stream = input("Enter stream:")
     names.append(name)
     ages.append(age)
     streams.append(stream)

stu_record = [names,ages,streams]
     

print(stu_record)

lis = [["ajay","raj","sohail","divya"],23,4,2]
lis[0].append("disha")
print(lis)
