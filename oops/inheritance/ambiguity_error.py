class Grandparents:

    def m(self):

        print("grandparent class m1 method")

class Parent:

    def m(self):

        print("parent class m2 method")

class Child(Grandparents,Parent):# here both define varible is m in grandparent and parent
                                #child call both but first is only display grandparent because 
       def m3(self):            #parent and grandparent variable is same so first call only display

        print("child class m3 method")

child_instance=Child()

child_instance.m3()

child_instance.m()

child_instance.m()