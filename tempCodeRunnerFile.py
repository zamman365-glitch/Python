class Animal:
    name = "Dog" #Class Attribute

    #Instance(Object) can never change your class attributes
    @classmethod
    def pookie(cls, new): #self -> Object
        cls.name = new
        print(cls.name)

obj = Animal()
obj.pookie("cat")