'''
decorator() -- wrapper function
generator() -- function that returns a generator object
it is a special category of functio which can generate the value and works as a iterator ,every generator f() must have atleast one yield keyword(statement)
yeild -- holds state and generate value 
(a sequence of values)
'''
def wrapper(f):
    def max_min(s,l):
        lis=f(s,l)
        print(lis)
        print("max",max(lis))
        print("min",min(lis))
        return lis
    return max_min


@wrapper
def create_list(size,lis) :
    for i in range(size):
        num = int(input("enter:"))
        lis.append(num)
    return lis

li = []
n = int(input("enter size:"))
result = create_list(n,li)
print(result)



def message():
    yield "welcome"
    yield "to"
    yield "python"
for i in message():
    print(i,end=" ")

#next()