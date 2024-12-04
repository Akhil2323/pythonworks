class Mobile():

    name=str

    price=int

    brand=str

    def __init__(self,name,price,brand):

        self.name=name

        self.price=price

        self.brand=brand

    def disply(self):

        print(self.name,self.price,self.brand)

mobile_instance=Mobile("iphone 15",55000,"apple")

mobile_instance.disply()