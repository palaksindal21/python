'''
mapping 
dict() - key, value
it is a mapping data type where we map a key element to its corresponding value element..
feature - 
ordered
mapping data 
Before version 3.6 : dictonaries were unordered
---collection of key value pair
Features of key --
1. key may be a container,single valued,
2.key should be unique
3.key must be immutable

4. Dictionaries are represented by - {key:vale,key1:value}

dict = {}
print(type(dict))

d = dict()
print(type(d))

dictionary = {1:"monday",2:"tuesday",1:"january"} #if the key names are same it will update the value
print(dictionary)
print(d[1]) #access
dictionary[1] = "jan"
print(dictionary)
#lhs = rhs
dictionary[2] = dictionary[1]
print(dictionary)
 #swapping 
dictionary[1],dictionary[2] = dictionary[2],dictionary[1]
print(dictionary)

dictionary[3] = "wednesday"  #add element to the dictionary
print(dictionary)

dictionary.update({4:"thursday"})
print(dictionary)

#functions and methods in dict'
'''
dict1 = {1:"mon",2:"tues",3:"wed"}

# for i in dict1 :
#     print(i)
#     print(i,dict1[i])
# #keys() ---> returns a view object that displays a list of all keys available in the dictionary
# #values() ----> returns a view object that displays a list of all values available in the dictionary
# #items() ------> returns a view object that displays a list of a tuple of a key value map

# keys = dict1.keys()
# print(keys,type(keys))
# values = dict1.values()
# print(values,type(values))
# items = dict1.items()
# print(items,type(items))

# for i in dict1.keys() :
#     print(i)

# for i in dict1.values() :
#     print(i)

# for i in dict1.items() :
#     print(i)

# #2 control values
# for i,j in dict1.items() :
#     print(i,j)

# list = [[1,2,3,4], [5,6,7,8]]
# for i,j,k,l in list :
#     print(i,j,k,l)

# #nested dictionary
# records = {
#     "101" : {"name" : "John", "age" : 25,"marks" :[20,23,25]},
#     "102" : {"name" : "akash", "age" : 24,"marks" :[18,20,30]},
#     "103" : {"name" : "avni", "age" : 23,"marks" :[21,23,30]},

# }
# print(records)
# records["101"].update({"stream":"science"})
# records["102"].update({"stream":"art"})
# records["103"].update({"stream":"commerce"})
# print(records)
# print(records["101"])
# records["103"].update({"marks":[21,88,30]})
# print(records["103"])
# records["103"]["marks"][1] = 88
# print(records["103"])

#pop() popitem() setedfault()
dic = {1:223,2:34,3:456}
deleted_value = dic.pop(2)
print(dic,deleted_value)
#popitem() removes the last inserted item
deleted_value = dic.popitem()
print(dic,deleted_value)

#setdefault()
#key value available: no changes, corresponding value return
#key value not available: changes(add key-value pair), return new value
dic1= {1:223,2:34,3:456}
result = dic1.setdefault(4, 100) #django environment
print(dic1)
print(result)

result = dic1.setdefault(1,223)
print(dic1)
print(result)

#get()  -----> return value
result = dic.get(2)
print(result)

result = dic.get(22) #return none if key is not present in the dictionary
print(result) 

# result = dic[22] # subscript operator
# print(result)

# key = int(input())
# if dic.get(key):
#     result = dic.get(key)
#     print(result)

dict2 = {1:"mon",2:"tue",6:"sat",7:"sun"}
dic2 = {3:"wed",4:"thurs",5:"fri"}
dict3 = {}#merge two dictionaries
for i in dict2 :
     dict3[i] = dict2[i]
     if i == 2 :
          dict3.update(dic2)
        
print(dict3)

d = {1:"mon",2:"tue",6:"sat",7:"sun"}
d1 = {3:"wed",4:"thurs",5:"fri"}
k = {}
keys = sorted(list(d.keys()) + list(d1.keys()))
print(keys)
for i in keys :
     if i in d :
          k[i] = d[i]
     elif i in d1 :
          k[i] = d1[i]
print(k)
