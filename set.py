#set - it is a collection of unique elements. In python set is categorized as unordered mutable data type where the data is more crucial than the order than we use set data type.
#Representation : {element1, element2, element3, element4, element5}
#Operations : union, intersection, difference, symmetric_difference, add, discard, pop, remove,
s1 = set() #empty set
s2 = {1, 2, 3, 4, 5,6,7,8,9} #set with elements
print(type(s2))

if 6 in s1 :
    print(6)

s2.add(10)
print(s2)

s2.remove(1) #return none
s2.discard(10)#return none
print(s2)
set = {10,12,1,2,3,4,56}
s3 = s1|s2
s4 = set & s2
s5 = set - s1
print(s3,s4,s5)
print(s3)
t = [50,40,30,20]
set.update(s2)
print(set)