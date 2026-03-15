#Higher order function 
#filter(), map(), reduce(), lambda()
'''
filter() - 
reduce() - used on multiple items reduce(function,iterator)
'''
def find_even(a):

    # for i in li():
    #     if i%2==0:
    #         print(i,end=" ")
    if a % 2 == 0:
      return a
lis = [22,33,4,5,6]

find_even(lis)
print(lis)

a = list(filter(find_even,lis))
print(a)

# from functools import reduce

# def add(a,b) :
#     return a+b
# def great(a,b):
#     if a>b :
#        return a
#     else:
#        return b
# lis = [22,33,4,5,6]
# a = reduce(great,lis)
# print(a)


#find out the employee with highest salary

# from functools import reduce
# records = [
#     [101,"mihir",45000],
#     [102,"shubham",50000],
#     [103,"krish",40000]
# ]

# def salary(a,b) :
#     if a[2]>b[2] :
#         return a
#     elif b[2]>a[2] :
#         return b
# c = reduce(salary,records)
# print(c)


