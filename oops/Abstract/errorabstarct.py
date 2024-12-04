# abstractmethod is call all fuction call in method otherwise error occur
# in hunter bike stop method not call all other ,their error occure becuase of abstract method call
# atleast one method is not called error occur.so all method call to avoid error

from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod    
    def stop(self):
        pass

class Hunter(Bike):

    def start(self):
        print("hunter start method")

    def accelerate(self):
        print("hunter accelerate method")

    # def stop(self):
    #     print("hunter stop method")

Hunter_instance=Hunter()

Hunter_instance.start()