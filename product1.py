class Product :
    def __init__(self) :
        self.name = input("Enter Product Name : ")
        self.price = int(input("Enter Product Price : "))
        self.quantity = int(input("Enter Product Quantity : "))
        self.total = self.price * self.quantity
    def total_price(self):
        print("total price is",self.total)
obj1 = Product()
obj1.total_price()