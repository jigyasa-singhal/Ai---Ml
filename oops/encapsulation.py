class BankAccount:
    def __init__(self,name,balance,acctype):
        self.name = name        #public attribute 
        self.__balance = balance #private  attribute
        self._acctype = acctype #protected attribute 




    def get_balance(self):#getter fn to access the balance 
        return self.__balance

    def set_balance(self,new_balance): #setter fn to set&access the balance 
        self.__balance = new_balance
    
# protected acess same as the private  attributes but private can't
# private attribuets  can access by two ways 1.name-mangled 2.by getter-setter

acc1 = BankAccount("ram",12_000,"current")
print(acc1.name,acc1._acctype) #access of private and protected attributes


# print(acc1.__balance)          # Wrong → AttributeError

print(acc1._BankAccount__balance) # Correct → name-mangled a ttribute 
print("previous balance",acc1.get_balance())                                                                    
(acc1.set_balance(20000)) 
print("current balance",acc1.get_balance())


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):        # getter
        return self.__balance

    @balance.setter
    def balance(self, amount):  # setter
        self.__balance = amount


acc1 = BankAccount(12000)

print(acc1.balance)   # calls getter → 12000

acc1.balance = 20000  # calls setter → updates balance

print(acc1.balance)   # calls getter → 20000
