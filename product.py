purchase = int(input("Enter purchase amount:"))

if purchase <= 100 :
    print("You have to pay",purchase)
elif purchase > 100 and purchase <= 500 :
    discount = purchase * 10/100
    print("You have to pay ",purchase - discount)
elif purchase > 500 and purchase <= 1000 :
    discount = purchase * 20/100
    print("You have to pay ",purchase - discount)
else :
    discount = purchase * 30/100
    print("You have to pay ",purchase - discount)