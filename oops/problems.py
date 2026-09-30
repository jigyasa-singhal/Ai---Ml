class Products:
    count = 0 
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Products.count+=1

    def get_info(self):
        print(f"product is {self.name} and price is {self.price}")

    @staticmethod
    def discount(price,a):
        final_price = price-(price*a/100)
        print(final_price)

    @classmethod    
    def get_count(cls):
        print(f"count of objects is {cls.count}")

pd1 = Products("tv",34000)
pd1 = Products("phone",34000)


print(pd1.name)
print(pd1.__dict__)
Products.discount(34000,12)
Products.discount(pd1.price,12)

Products.get_count()