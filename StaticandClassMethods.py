"""class Sample:
    a = "Chacha"

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("This is a constructor....")
        print(self.name)
        print(self.age)

obj = Sample("Amit",18)
"""


#1. classmethod
class Animal:
    name = "Dog" #Class Attribute

    #Instance(Object) can never change your class attributes
    @classmethod
    def pookie(cls, new): #self -> Object
        cls.name = new
        print(cls.name)

obj = Animal()
obj.pookie("cat")












#2. staticmethod
"""class SharmaVishnu:
    @staticmethod #Independent of object, mtlb object bane ya na bane ghanta farak nahi pdta
    def menu():
        print("Paneer kulche")
        print("Paneer tikka")
        print("Paneer cheese sandwich")
        print("Cold Coffee")

# Without object
SharmaVishnu.menu()

# with object
new_market = SharmaVishnu()
new_market.menu()"""
class Animal:
    name = "Dog" #Class Attribute

    #Instance(Object) can never change your class attributes
    @classmethod
    def pookie(cls, new): #self -> Object
        cls.name = new
        print(cls.name)

obj = Animal()
obj.pookie("cat")