n=int(input("Enter number of rows: "))
for i in range(1, n+1):   
    print("*"*n)


n=int(input("Enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i,end=" ")   #print one number in same row
    print()
   

n=int(input("Enter number of rows: "))
for i in range(1, n+1):  #print rows
    for j in range(1, n+1):  #print columns
        print(j,end=" ")  #print one number in one column
    print()

n=int(input("Enter number of rows:"))
for i in range(1,n+1):  #print alphabets in rows
    for j in range(1,n+1):  #print alphabets in columns
        print(chr(64+i),end=" ")   #print alphabet by ASCII value
    print()

n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=" ")
    print()