'''
frozen set : immutable object
unordered data type
application
data is important but order is not important, no modifications
frozen set is used in hash table, dictionary, set, etc.
used to create a dictionary keys..
in set and frozen set speed is faster than list and tuple
'''



s1 = {"a","e","i","o","u"}
s2 = {"a","e","u",1,2}

f1 = frozenset(s1)
print(f1)
f2 = frozenset(s2)

f3 = f1|f2 #union
f3 = f1&f2 #intersection
f3 = f1-f2 #set difference
f3 = set(f3)
f4 = frozenset([2,3,4,5,6,7,8])
print(f4)
print(type(f3))