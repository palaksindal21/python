# WAP to capitalized each element of a given tuple t.
t = ("apple","banana","pineapple")
lis = list(t)
print(lis)

'''
k = 0
for i in lis:
    lis[k] = i.capitalize()
    k = k+1
'''
for i in range(len(lis)) :
    lis[i] = lis[i].capitalize()
t = tuple(lis)
print(t)


t = [11,22,3,44,"apple",3,-4,5.5,True,"banana",33,56,11]
s1 = t[0:5]
s2 = t[9:]
s3 = s1+s2
print(s1)
print(s2)
print(s3)

# slicing [start : end : step ]
#    0  1  2  3   4     5  6  7   8      9     10 11 12
t = [11,22,3,44,"apple",3,-4,5.5,True,"banana",33,56,11]
#   -13 -12  -10 -9    -8    -6   -5    -4    -3  -2  -1

print(t)
s1=t[4:10] # t[-9:-3] -->['apple', 3, -4, 5.5, True, 'banana']
s2=t[4:10:2] #t[-9:-3:2]--> ['apple', -4, True]
s3=t[9:3:-1] # t[-4:-10:-1]['banana', True, 5.5, -4, 3, 'apple']
s4=t[10:2:2] # []
s5=t[4:] #['apple', 3, -4, 5.5, True, 'banana', 33, 56, 11]
s6=t[4::2]#['apple', -4, True, 33, 11]
s7=t[4:-3:2]#['apple', -4, True]
s8=t[9::-1]# ['banana', True, 5.5, -4, 3, 'apple', 44, 3, 22, 11]
s9=t[::2]#[11, 3, 'apple', -4, True, 33, 11]
s10=t[::-1]#[11, 56, 33, 'banana', True, 5.5, -4, 3, 'apple', 44, 3, 22, 11]
print(s10)



n = int(input("how many record do u want to insert:"))#4
stu_records = [[],[],[]]

for i in range(n):
    name = input("Enter name:")
    age = int(input("Enter age:"))
    stream = input("enter stream:")
    stu_records[0].append(name)
    stu_records[1].append(age)
    stu_records[2].append(stream)
print(stu_records)

# tuple:
# 1)container
# 2)immutable
# 3)ordered data -type
# 4)heterogenous(repetation allowed)
# 5)faster work as compared to list.
# 6)representation -->()

t1 = (22,3,"wwww")
print(type(t1))
print(t1)
print(t1[1])
t1[2]= 90

t1 = "apple"
print(t1)


t1 = 22,3,88,9
print(type(t1))
# single element
t2 = (23,)
print(type(t2))



t1 = (2,3,4,5)
del t1
t1=9
print("w")

# count(),index(),min(),max(),sum(),
# 


# . method (define class)
# function -->len() ,sorted()

t1 = (-9,2,3,4,4,-5,44,3)
lis = sorted(t1) # return sorted list
print(t1)
print(lis)


#WAP to capitalized each element of a given tuple t.
t = ("appLE","baNAna","pineApple")
lis = list(t)
print(lis)
'''
k=0
for i in lis:
    lis[k]=i.capitalize()
    k = k+1
'''
for i in range(len(lis)):
     lis[i]=lis[i].capitalize()
t= tuple(lis)
print(t)





#a="raHUL"
#print(a.capitalize())



















