# # string - it is a sequence of characters
# # immutable
# # ordered

s = "python"
print(s)
s = list(s)
print(s)

s[2]="r"
s="".join(s)
print(s,"wwwww")


# #method of string-->
# # lower(), upper(), isalpha(), isdigit(), capitalize(), isupper(), islower(),

s = "apple is good for health"
output = s.isalpha()
output1 = s.lower()
output2 = s.upper()
output3 = s.capitalize()
output4 = s.islower()
output5 = s.isupper()
output6 = s.isalnum()
output7 = s.isascii()
output8 = s.istitle()
print(output)

# # split() -->string method  , return list
t = "apple is good for health"
lis = t.split("good",2)
list = t.split("good")
li = t.split(" ",2)
print(lis)
print(list)
print(li)

# # join() --> string method , return string, iterable input
# # join() ---> take list as input and return a string...

# list = ["apple","banana","pineapple","orange"]
# output9 = " ".join(list)
# print(output9)
# # output9 = "".join(list)
# l = "apple"
# output10 =" ".join(l)
# print(output10)

# # format()
length = 10
breadth = 12
area = length * breadth
# print("area of rectangle is {} ".format(area))
a = "length: {} breadth: {} area: {}".format(length,breadth,area)
print(a)

# # replace() = replace(old,new)

# #method of string .
# # lower(),upper(),capitalize(),--> return string
# # isalpha(),isdigit() ,isupper() ,islower(),---->boolean (True /False)

# s = "apple is good 4 health"

# output = s.lower()
# print(output)

# s = "apple is good 4 health"

# output = s.isalpha()
# print(output)

# s = "apple is good 4 health"

# output = s.capitalize()
# print(output)

# s = "apple is good 4 #$%^&*&^%$#@ hEalth"

# output = s.islower()
# print(output)

# # split()  --> string method
# #        --> return list
# #  join() 

# s = "apple is good 4 health"
# lis = s.split(" ",2)
# print(s)
# print(lis)

# #  join() ->iterable(element string) input
#         # return string

# lis = ["apple","banana","pineapple","orange","90"]


# s=" and ".join(lis)
# print(s)

# s = "222222222222 33333333333"

# output = s.isdigit()
# print(output)

# length = 90
# bredth = 12

# area = length*bredth

# print("length:",length,"breadth:",bredth,"Area:",area)

# a="length: {2} breadth: {0} Area: {2}".format(2*length,bredth,area)
# print(a)

# #  replace(old,new)

# s= "apple is good for health,banana is good for "
# s=s.replace("good","bad",1)
# print(s)

#split #join()
#index(),count()
s1 = "its now or never"
#output = "sti.won.ro.reven"
# for i in range(len(s1)) :
#     print(s1[i],"-------->",i)

# print(s1.index("w"))

list = s1.split(" ")
li = []
for i in list:
        a = i[::-1]
        li.append(a)
        print(li)  # Output: it, now, or, never
s = ".".join(li)
print(list)
print(s)
print(li)

