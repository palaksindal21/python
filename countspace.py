# Q.1: WAP to count space in the following string S.
S="we are here to learn dsa"
s = S.count(" ")
print(s)S

# Q.2: WAP to count number of upper letters and lower letters in the following string S.
#S= ”WE ARE HERE TO learn DSA”
S="WE ARE HERE TO learn DSA"
for i in S :
    if i.isupper():
        I=S.count(i)
        
    else :
        J=S.count(i)
        
print(I)
print(J)

# Q.3: WAP to swap the upper letters with lower letters and lower with upper in the following string S.
# And also replace space with character ‘$’.
# S= ”WE ARE HERE TO learn DSA”
A = "WE ARE HERE TO learn DSA"
B = A.replace(" ","$")
for i in A :
    if i.isupper():
      I = i.lower()
      B = B.replace(i, I)
    elif i.islower():
      I = i.upper()
      B = B.replace(i, I)     
print(B)

# Q.1) WAP  to reverse a string  s with the following condition.
# =”we are here to learn dsa”

# A)	reverse whole string.
# Output: “asd nrael ot ereh era ew”
c = "we are here to learn dsa"
list1 = c.split(" ")
li = []
for i in list1 :
  li.append(i[::-1])
S = li[::-1]
print(S)
string = " ".join(S)
print(string)

# B)	  to reverse the order of the words in the given string.
# Output: “dsa learn to here are we”
P = "we are here to learn dsa"  
list2 = P.split(" ")
print(list2)
list3 = list2[::-1]
string2 = " ".join(list3)
print(string2)

# C)     to reverse the words in the given string in the original order.
# Output: “ew era ereh ot nrael asd ”
P = "we are here to learn dsa"  
list4 = P.split(" ")
empli = []
for i in list4:
    a = i[::-1]
    empli.append(a)
empli1 = " ".join(empli)
print(empli1)
    
# Q.2) WAP  to capitalize the first and last character of each word in a string.
#       S=”we are here to learn dsa”
# Output: ”WE ArE HerE TO LearN DsA”
Q = "we are here to learn dsa"
list5 = Q.split(" ")
li = []
for i in list5 :
    li.append(i[0].upper()+i[1:-1].lower()+i[-1].upper())
    
print(li)
output = " ".join(li)
print(output)