class Grandparents:

    def m1(self):

        print("grandparent class m1 method")

class Parent:

    def m2(self):

        print("parent class m2 method")

class Child(Grandparents,Parent):#this is multiple inheritance

    def m3(self):

        print("child class m3 method")

child_instance=Child()

child_instance.m3()

child_instance.m2()

child_instance.m1()