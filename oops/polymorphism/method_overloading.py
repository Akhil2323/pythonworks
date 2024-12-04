# methodoverloading not support in python

class Operation:
            
    def add(self,num1,num2): #this do not work because python is interpreted language
                    
        print(num1+num2)
                                            
    def add(self,num1,num2,num3):
                    
        print(num1+num2+num3)

obj=Operation()

obj.add(10,20,30)

obj.add(10,20)