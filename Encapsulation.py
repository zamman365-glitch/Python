                       # public 
class Animal:
    name="Lion"   # public Attributes
    def speaks(self):  # public object method 
        print("the lion roars")
    
obj1=Animal()
obj1.speaks()

                        # protected
class Animal:
    name="Lion"   # public Attribute
    _age=12     # protected attribute


    def speaks(self):   # public object method 
        print("the lion roars")
    
    def _walk(self): # protected object method
        print("the lion is walking ")

    
obj1=Animal()
obj1.speaks()



                       # private
class Animal:
    name="Lion"   # public Attribute
    _age=12     # protected attribute
    __weight=120   # private attribute


    def speaks(self):   # public object method 
        print("the lion roars")
    
    def _walk(self): # protected object method
        print("the lion is walking ")

    def __sleep(self):  # private object method
        print("the lion is sleeping")

    
obj1=Animal()
# print(obj1._height)    # mgr iska koi mtlb nhi hoga because yeh private hai height 
# obj1.__sleep()

#private attributes and method cannot be accessed by
#your object and inherited class