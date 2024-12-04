from abc import ABC,abstractmethod

class Bank():
    
    def __init__(self,customer_name,mpin,balance,account_type):
        self.customer_name=customer_name
        self.__mpin=mpin
        self.__balance=balance
        self.account_type=account_type
    
    def _str_(self):
        return self.customer_name
    
    def get_bal(self):
        print(self.__balance)

    
bank_acc_instance=Bank("Rogan","3399",100000000,"savings")

# print(bank_acc_instance.mpin)  /#we can't access the pin since it is private attribute so we create method for it
print(bank_acc_instance)
bank_acc_instance.get_bal()  #here we call the method to return balance to access balance, we can't access the 
                             #variable  "__balance" since it is prvt