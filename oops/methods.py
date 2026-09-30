class Laptops:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage


# instance method - can access instance attributes and class attributes by self
    def get_info(self):
        print(f"Laptop has {self.RAM} and stroage is {self.storage} and {self.storage_type}")

# class method

    @classmethod
    def get_storage_type(cls):
         print(f"Laptop has  {cls.storage_type}")

# static methods 
    @staticmethod
    def discount(price,discount):
        final_price = price-(discount*price/100)
        print(final_price)





l1 = Laptops("36gb","512gb")
l2 = Laptops("32gb","256gb")

# instance method call
print(l1.RAM)
l1.get_info()        # by the object name itself 
Laptops.get_info(l1) #calling is by class name by passing object in it 

# class method call
l1.get_storage_type()       # All laptops use SSD
Laptops.get_storage_type() 

l1.discount(40000,34)
Laptops.discount(34000,45)


