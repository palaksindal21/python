'''
scope of variable
global variable
local variable
NOTE - if you we to take access of global variable in function body then it must be defined earlier than function call.
NOTE- we can't take access of local variable in global scope but vice versa is possible.
'''
def add() :
    a = 90
    b = 23
    mssg = "local variable" #locality of reference
    print("sum",a+b)
    print(mssg)

mssg = "global variable"
add()

def sum():
    global msg
    msg = "global variable"
sum()
print(msg)

'''
Default arguments
'''
def Add(a,b,c,d=0) :
    print("add:",a+b+c+d)
Add()
#parameter without a default follows parameter with a default