"""
class SharmaVishnu:
    def sample():    # class ke andar ke function ko method bolte hai 
        print('this is sample function ')
    
SharmaVishnu.sample() 
"""


                                 #CLASS 
"""                                
class SharmaVishnu:
        a='lolo'      # class ke andar variable ko bolte hai Attributes

        def sample():
             print('this is a sample function ')
   
        print('this is sample function ')
    
SharmaVishnu.sample()
print(SharmaVishnu.a)

"""



                             #OBJECT
"""
class  Animal:
    #attrirutes
    name="animal"
    

    def greet(self):   # ki jab bhi class ke andar ke function ko object ke help se call karoge toh ek PARAMETER set karna padega 

        print("This is animal class")


chacha=Animal()  #here chacha is object.
mama=Animal()
chacha.greet()
print(chacha.name)

#object ka naam same as hota hai as name of the variable
# ke class ke mutiple object ho skte hai 


# create a class which will perform 2 tasks
# 1. greet the user -"this is ----class"
# 2. adding up two number

class Lolo:
    def greet(self):
        print("this is a class")
    def add(self,a,b):
        print(a+b)
        
obj=Lolo()
obj.greet()
obj.add(10,20)

"""




                              # CONSTRUCTOR

#constructor -> represented by __init__(Dunder Methods)
#constructor sabse phele execute hone wala function hai does'nt matter inke upar ya neeche koi function present hai 
"""class SharmaVishnu:
    def __init__(self):
        print("This is a constructor")
    def menu(self):
        print('Paneer khulche')

obj =SharmaVishnu()
obj.menu() """   # call karne par phele constructor call hoga phir baad mei method or function 



#object ke help se koi naye attributes create karne hai
#obeject or instant attributes

"""class SharmaVishnu:
    def __init__(self,name,age):
        self.name=name   #Instant attributes
        self.age=age 
        print("This is a constructor")
    def menu(self):
        print(self.name)
        print(self.age)
        print('Paneer khulche')

obj =SharmaVishnu("Chacha",21)
obj.menu() 
"""



"""class SharmaVishnu:
    def __init__(lolo,name,age):
        lolo.name=name   #Instant attributes
        lolo.age=age 
        print("This is a constructor")
    def menu(lolo):
        print(lolo.name)
        print(lolo.age)
        print('Paneer khulche')

obj =SharmaVishnu("Chacha",21)
obj.menu()""" 



# make a class which will take 2 number as input create
# 1. instant attritubes
# 2. create a function which will print greatest amoung then

"""class Sharma:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        if self.a>self.b:
            print("a is greater",self.a)
        else:
            print(" b is greater",self.b)

obj=Sharma(20,30)

"""



"""class Laxit:
    def __init__(self):
        print("This is the Laxit class")

    def greet(self,a,b):
        print(f"The sum of {a} and {b} is {a+b}")
    
    def __init__(self):
        print("This is another constructor function")
    
    def greet(self,name):
        self.name = name #Instance Attribute
        print(f'hello {self.name}')


obj = Laxit()
obj.greet(":Laxit")""" 
 

