"""def Hello():
    print("hello how are you ")

def Hello():
    print("hello again")"""


class Animal:
    def speak(self):
        print("animals are shouting")
class Human:
    def human(self):
        print("humans are intelligent")


obj1=Animal()
obj2=Human()

obj1.speak()
obj2.human()
# both the speaks method appears to be same but both have different task and this is known polymorphism








                                    # method overriding
class Reebok:
    def __init__(self,material,size):
        self.material=material
        self.size=size
    
    def details(self):
        print("your bag detail is :")
        print(self.material)
        print(self.size)

class campus(Reebok):
    def __init__(self,material,size,color):
        super().__init__(material,size)
        self.color=color

    def details(self):
        print()
        print (super().details())
    
obj1=campus("leather",10,"black")

obj1.details()


"""
a child class object has the power to call methods and 
attributes of a parent class but he cannot call the details
methods of his parent class cause that details methods is overridden and this concept is known as method
overriding
"""



                                    # overloading
# python mei overloading nhi hoti hai